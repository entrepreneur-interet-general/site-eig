---
layout: post
modal-id: "Entrée de blog technique : Tensorflow par Victor Schmidt"
author: Victor Schmidt, EIG Hopkins 
twitter: Vict0rSch
description: "Victor Schmidt est datascientist et EIG dans le défi Hopkins.  Il publie des articles techniques sur https://vict0rsch.github.io pour apprendre et partager ce qu'il apprend.  Dans cette entrée de blog technique, il nous met dans la situation d'un développeur cherchant à corriger un problème qu'il rencontre avec son code."
---

# Pourquoi une entrée de blog technique ?

*Le programme EIG mise sur l'efficacité d'équipes restreintes, où les
personnes ayant des compétences techniques (designers, développeurs ou
analystes de données) travaillent en lien étroit avec les experts d'un
service de l'administration.  Le dialogue qui se noue exige, pour être
efficace, d'ajuster les fins (des mentors) aux moyens (des EIG) : cet
ajustement est plus efficace quand les EIG se familiarisent vite avec
le domaine métier des mentors, et quand les mentors comprennent quels
moyens sont mobilisables par les EIG.*

*Avec cet article de Victor, le blog EIG accueille des articles plus
techniques : nous sommes persuadés qu'il est important de comprendre
comment les développeurs abordent leurs problèmes pour travailler avec
eux.  Nous souhaitons aussi que ce blog participe du vaste dialogue
technique que la culture de l'open source aide à nourrir.*

# [Titre]

## [Introduction]

Je me suis récemment retrouvé dans une situation difficile.  Bien
qu'avec `tf.saved_model.simple_save` et `tf.saved_model.loader.load`
il n'ait jamais été aussi facile de sauvegarder ou de charger un
modèle Tensorflow, il existe peu de documentation sur l'interaction
entre ces fonctions et l'API Dataset, particulièrement sur la façon
restaurer l'`Iterator` d'un `tf.data.Dataset`.

Ce post contient du code autonome et déterministe parce qu'il n'y a
pas mieux qu'un bon exemple pour apprendre : j'y crée un modèle, le
sauvegarde, le restaure dans un nouveau graph et vérifie que les
inférences concordent. Le code est écrit pour python 3 et Tensorflow
1.8.

## [Code]

Ci après, un exemple minimal de code autonome. J'utilise des données
aléatoires parce que ce n'est qu'une démonstration:

1. On commence par créer les `placeholder`. Ils contiendront les
   données à l'exécution du graph. À partir de ceux-ci, on crée un
   `Dataset` et son `Iterator` associé. On en extrait le Tensor généré
   en sortie, `input_tensor` qui servira d'entrée au modèle.
   
2. Le modèle en question est un RNN bi-directionnel (GRU) suivi d'un
   classifier dense en sortie. Parce que pourquoi pas.
   
3. La fonction de coût est une `softmax_cross_entropy_with_logits`
   optimisée par `Adam`. Après 2 epochs (de 2 batchs chacune), le
   modèle "entrainé" est sauvegardé avec
   `tf.saved_model.simple_save`. [Si vous exécutez le code tel quel,
   le model sera créé dans un dossier `./simple/`]
   
4. Dans un nouveau graph, on restaure le modèle sauvegardé avec
   `tf.saved_model.loader.load`. Les placeholders et logits sont
   extraits avec `graph.get_tensor_by_name` et l'opération
   d'initialisation de l'`Iterator` grâce à
   `graph.get_operation_by_name`.
   
5. Enfin, on compare l'inférence des deux modèles pour chaque batch
   dans le dataset et on vérifie que le modèle sauvegardé et le
   restauré produisent les mêmes valeurs. Ça marche !

{% highlight python %}
import os
import shutil
import numpy as np
import tensorflow as tf
from tensorflow.python.saved_model import tag_constants

def model(graph, input_tensor):
    """Create the model which consists of
    a bidirectional rnn (GRU(10)) followed by a dense classifier

    Args:
        graph (tf.Graph): Tensors' graph
        input_tensor (tf.Tensor): Tensor fed as input to the model

    Returns:
        tf.Tensor: the model's output layer Tensor
    """
    cell = tf.nn.rnn_cell.GRUCell(10)
    with graph.as_default():
        ((fw_outputs, bw_outputs), (fw_state, bw_state)) = tf.nn.bidirectional_dynamic_rnn(
            cell_fw=cell,
            cell_bw=cell,
            inputs=input_tensor,
            sequence_length=[10] * 32,
            dtype=tf.float32,
            swap_memory=True,
            scope=None)
        outputs = tf.concat((fw_outputs, bw_outputs), 2)
        mean = tf.reduce_mean(outputs, axis=1)
        dense = tf.layers.dense(mean, 5, activation=None)

        return dense

def get_opt_op(graph, logits, labels_tensor):
    """Create optimization operation from model's logits and labels

    Args:
        graph (tf.Graph): Tensors' graph
        logits (tf.Tensor): The model's output without activation
        labels_tensor (tf.Tensor): Target labels

    Returns:
        tf.Operation: the operation performing a stem of Adam optimizer
    """
    with graph.as_default():
        with tf.variable_scope('loss'):
            loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(
                    logits=logits, labels=labels_tensor, name='xent'),
                    name="mean-xent"
                    )
        with tf.variable_scope('optimizer'):
            opt_op = tf.train.AdamOptimizer(1e-2).minimize(loss)
        return opt_op

if __name__ == '__main__':
    # Set random seed for reproducibility
    # and create synthetic data
    np.random.seed(0)
    features = np.random.randn(64, 10, 30)
    labels = np.eye(5)[np.random.randint(0, 5, (64,))]

    graph1 = tf.Graph()
    with graph1.as_default():
        # Random seed for reproducibility
        tf.set_random_seed(0)
        # Placeholders
        batch_size_ph = tf.placeholder(tf.int64, name='batch_size_ph')
        features_data_ph = tf.placeholder(tf.float32, [None, None, 30], 'features_data_ph')
        labels_data_ph = tf.placeholder(tf.int32, [None, 5], 'labels_data_ph')
        # Dataset
        dataset = tf.data.Dataset.from_tensor_slices((features_data_ph, labels_data_ph))
        dataset = dataset.batch(batch_size_ph)
        iterator = tf.data.Iterator.from_structure(dataset.output_types, dataset.output_shapes)
        dataset_init_op = iterator.make_initializer(dataset, name='dataset_init')
        input_tensor, labels_tensor = iterator.get_next()

        # Model
        logits = model(graph1, input_tensor)
        # Optimization
        opt_op = get_opt_op(graph1, logits, labels_tensor)

        with tf.Session(graph=graph1) as sess:
            # Initialize variables
            tf.global_variables_initializer().run(session=sess)
            for epoch in range(3):
                batch = 0
                # Initialize dataset (could feed epochs in Dataset.repeat(epochs))
                sess.run(
                    dataset_init_op,
                    feed_dict={
                        features_data_ph: features,
                        labels_data_ph: labels,
                        batch_size_ph: 32
                    })
                values = []
                while True:
                    try:
                        if epoch < 2:
                            # Training
                            _, value = sess.run([opt_op, logits])
                            print('Epoch {}, batch {} | Sample value: {}'.format(epoch, batch, value[0]))
                            batch += 1
                        else:
                            # Final inference
                            values.append(sess.run(logits))
                            print('Epoch {}, batch {} | Final inference | Sample value: {}'.format(epoch, batch, values[-1][0]))
                            batch += 1
                    except tf.errors.OutOfRangeError:
                        break
            # Save model state
            print('\nSaving...')
            cwd = os.getcwd()
            path = os.path.join(cwd, 'simple')
            shutil.rmtree(path, ignore_errors=True)
            inputs_dict = {
                "batch_size_ph": batch_size_ph,
                "features_data_ph": features_data_ph,
                "labels_data_ph": labels_data_ph
            }
            outputs_dict = {
                "logits": logits
            }
            tf.saved_model.simple_save(
                sess, path, inputs_dict, outputs_dict
            )
            print('Ok')
    # Restoring
    graph2 = tf.Graph()
    with graph2.as_default():
        with tf.Session(graph=graph2) as sess:
            # Restore saved values
            print('\nRestoring...')
            tf.saved_model.loader.load(
                sess,
                [tag_constants.SERVING],
                path
            )
            print('Ok')
            # Get restored placeholders
            labels_data_ph = graph2.get_tensor_by_name('labels_data_ph:0')
            features_data_ph = graph2.get_tensor_by_name('features_data_ph:0')
            batch_size_ph = graph2.get_tensor_by_name('batch_size_ph:0')
            # Get restored model output
            restored_logits = graph2.get_tensor_by_name('dense/BiasAdd:0')
            # Get dataset initializing operation
            dataset_init_op = graph2.get_operation_by_name('dataset_init')

            # Initialize restored dataset
            sess.run(
                dataset_init_op,
                feed_dict={
                    features_data_ph: features,
                    labels_data_ph: labels,
                    batch_size_ph: 32
                }

            )
            # Compute inference for both batches in dataset
            restored_values = []
            for i in range(2):
                restored_values.append(sess.run(restored_logits))
                print('Restored values: ', restored_values[i][0])

    # Check if original inference and restored inference are equal
    valid = all((v == rv).all() for v, rv in zip(values, restored_values))
    print('\nInferences match: ', valid)
{% endhighlight %}

```
$ python3 save_and_restore.py

Epoch 0, batch 0 | Sample value: [-0.13851789 -0.3087595   0.12804556  0.20013677 -0.08229901]
Epoch 0, batch 1 | Sample value: [-0.00555491 -0.04339041 -0.05111827 -0.2480045  -0.00107776]
Epoch 1, batch 0 | Sample value: [-0.19321944 -0.2104792  -0.00602257  0.07465433  0.11674127]
Epoch 1, batch 1 | Sample value: [-0.05275984  0.05981954 -0.15913513 -0.3244143   0.10673307]
Epoch 2, batch 0 | Final inference | Sample value: [-0.26331693 -0.13013336 -0.12553    -0.04276478  0.2933622 ]
Epoch 2, batch 1 | Final inference | Sample value: [-0.07730117  0.11119192 -0.20817074 -0.35660955  0.16990358]

Saving...
INFO:tensorflow:Assets added to graph.
INFO:tensorflow:No assets to write.
INFO:tensorflow:SavedModel written to: b'/some/path/simple/saved_model.pb'
Ok

Restoring...
INFO:tensorflow:Restoring parameters from b'/some/path/simple/variables/variables'
Ok
Restored values:  [-0.26331693 -0.13013336 -0.12553    -0.04276478  0.2933622 ]
Restored values:  [-0.07730117  0.11119192 -0.20817074 -0.35660955  0.16990358]

Inferences match:  True
```

## FailedPreconditionError

Avant d'atteindre ce code fonctionnel, je n'arrivais pas à régler
cette erreur:

```
FailedPreconditionError (see above for traceback): GetNext() failed because the iterator has not been initialized
```

J'ai mis du temps à trouver mon problème, à le formuler correctement.
J'ai commencé par poser plusieurs questions sur Stackoverflow, lu de
nombreux postes de blogs et je suis même allé juqsu'à la deuxième page
des résultats d'une requête Google !

La sauvegarde du graphe fonctionnait, son chargement *a posteriori*
aussi et j'en extrayais les bons Tensors. Qu'est-ce qui n'allait pas?

## Code initial

Pour l'exemple, voici le code schématique de ma procédure (attention,
ce code est **faux**):

Sauvegarde:

{% highlight python %}
features_ph = tf.Placeholder(...)
labels_ph = tf.Placeholder(...)

dataset = tf.data.Dataset.from_tensor_slices(
            (features_data_ph, labels_data_ph))
iterator = dataset.make_initializable_iterator()

input_tensor, labels_tensor = iterator.get_next()

logits = my_model_function(input_tensor)
opt_op = my_optimizing_function(logits, labels_tensor)

with tf.Session() as sess:
    sess.run(dataset_init_op, feed_dict={
        features_data_ph: some_numpy_values,
        labels_data_ph: some_other_numpy_values
    })
    # training
    ...
    tf.saved_model.simple_save(...)
{% endhighlight %}

Chargement du modèle sauvegardé:

{% highlight python %}
dataset = tf.data.Dataset.from_tensor_slices(
            (features_data_ph, labels_data_ph))
iterator = dataset.make_initializable_iterator()
input_tensor, labels_tensor = iterator.get_next()

with tf.Session() as sess:
    tf.saved_model.loader.load(...)

    restored_labels_data_ph = graph2.get_tensor_by_name(...)
    restored_features_data_ph = graph2.get_tensor_by_name(...)
    restored_logits = graph2.get_tensor_by_name(...)

    sess.run(iterator.initializer, feed_dict={
        restored_features_data_ph: some_numpy_values,
        restored_labels_data_ph: some_other_numpy_values
    })

    restored_logits.eval(session=sess)
>>> "FailedPreconditionError (see above for traceback): GetNext() failed because the iterator has not been initialized [...]"
{% endhighlight %}

Alors, qu'est-ce qui ne va pas?

## Initialisation de l'Iterator

`tf.saved_model.simple_save` fixe les variables d'un graphe à partir
des valeurs d'une session. Quand on appelle
`tf.saved_model.loader.load`, les variables sont restaurées dans le
graph par défaut. Cependant, en appelant `iterator.initializer`, je
n'initialise pas l'`Iterator` **restauré** mais le **nouveau**! Comme
`restored_logits` dépend toujours de l'`input_tensor` du graph
restauré, qui lui même est issu de l'`Iterator` de ce même graph,
Tensroflow plante: on appelle un Tensor qui dépend d'un `Iterator` non
initialisé puisque j'ai initialisé le mauvais.

Il faut donc trouver la bonne opération d'initialisation dans le graph
restauré. Une manière simple de faire ça est de créer l'`Iterator`
d'une façon légèrement différente:

{% highlight python %}
dataset = tf.data.Dataset.from_tensor_slices((features_data_ph, labels_data_ph))
iterator = tf.data.Iterator.from_structure(dataset.output_types, dataset.output_shapes)
dataset_init_op = iterator.make_initializer(dataset, name='dataset_init')
input_tensor, labels_tensor = iterator.get_next()
{% endhighlight %}

Maintenant, l'opération en question est évidemment très facile à
retrouver dans le graph !

{% highlight python %}
dataset_init_op = graph.get_operation_by_name('dataset_init')
{% endhighlight %}

Et voilà :) C'est tout. Pas si compliqué ! Mais comme souvent les deux
étapes pour résoudre un problème sont :

1. Savoir formuler son problème
2. Comprendre ces **** d'erreurs Tensorflow
