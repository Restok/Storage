from __future__ import print_function
import numpy as np
import tensorflow as tf

#a constant one tf node. It stores a value, takes no inputs, and outputs the stored value
node1 = tf.constant(3.0, dtype=tf.float32)
node2 = tf.constant(4.0) # also tf.float32 implicitly
#Has to evaluate node with a session
sess = tf.Session()
print(sess.run([node1, node2]))
#outputs: [3.0, 4.0]
node3 = tf.add(node1, node2)
print(sess.run(node3))
#outputs 7
#A placeholder accepts an input, and promises to produce a value later.
a = tf.placeholder(tf.float32)
b = tf.placeholder(tf.float32)

adder_node = a+b

print(sess.run(adder_node, {a: [7, 9], b: [8, 10]}))

add_and_triple = adder_node * 3.
print(sess.run(add_and_triple, {a: 3, b: 4.5}))

M = tf.Variable([.3], dtype=tf.float32)
b = tf.Variable([-.3], dtype=tf.float32)
x = tf.placeholder(tf.float32)

init = tf.global_variables_initializer()
sess.run(init)
linear_equation = M*x + b

print(sess.run(linear_equation, {x:[1, 2, 3, 4, 5]}))

y = tf.placeholder(dtype=tf.float32)
squared_deltas = tf.square(linear_equation-y)

totalloss = tf.reduce_sum(squared_deltas)
print(sess.run(squared_deltas, {x:[1,2,3,4], y:[0, -1, -2,-3]}))
print(sess.run(totalloss, {x:[1,2,3,4], y:[0, -1,-2,-3]}))


print(sess.run(totalloss, {x:[1,2,3,4], y:[0, -1,-2,-3]}))

sess.run(init)

optimizer = tf.train.GradientDescentOptimizer(0.01)
train = optimizer.minimize(totalloss)
for i in range(1000):
	sess.run(train, {x:[1,2,3,4], y:[0, -1, -2, -3]})

print(sess.run([M, b]))

feature_columns = [tf.feature_column.numeric_column("x", shape=[1])]
estimator = tf.estimator.LinearRegressor(feature_columns=feature_columns)

x_train = np.array([1.,2.,3.,4.])
y_train = np.array([0., -1., -2., -3.])
x_eval = np.array([2., 5., 8., 1.])
y_eval = np.array([-1.01, -4.1, -7, 0.])


