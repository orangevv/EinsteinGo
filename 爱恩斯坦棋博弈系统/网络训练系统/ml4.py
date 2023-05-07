import numpy as np
import os
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import datasets,layers,optimizers,Sequential

conv_layers = conv_net = Sequential([
    layers.Conv2D(32, kernel_size=[3,3], padding="same", activation=tf.nn.relu),
    layers.Conv2D(32, kernel_size=[3,3], padding="same", activation=tf.nn.relu),
    layers.MaxPool2D(pool_size=[2, 2], strides=2, padding="same"),
    # unit2
    layers.Conv2D(64, kernel_size=[3, 3], padding="same", activation=tf.nn.relu),
    layers.Conv2D(64, kernel_size=[3, 3], padding="same", activation=tf.nn.relu),
    layers.MaxPool2D(pool_size=[2, 2], strides=2, padding="same"),
    # unit3
    layers.Conv2D(128, kernel_size=[3, 3], padding="same", activation=tf.nn.relu),
    layers.Conv2D(128, kernel_size=[3, 3], padding="same", activation=tf.nn.relu),
    layers.MaxPool2D(pool_size=[2, 2], strides=2, padding="same"),
    # unit4
    layers.Conv2D(500, kernel_size=[3, 3], padding="same", activation=tf.nn.relu),
    layers.Conv2D(500, kernel_size=[3, 3], padding="same", activation=tf.nn.relu),
    layers.MaxPool2D(pool_size=[2, 2], strides=2, padding="same")
])

fc_net = Sequential([
    layers.Dense(400, activation=tf.nn.relu),
    layers.Dense(200, activation=tf.nn.relu),
    layers.Dense(50, activation=tf.nn.relu),
    layers.Dense(18, activation=None)
])

def preprocess(x, y):
    x = tf.cast(x, dtype=tf.float32)
    y = tf.cast(y, dtype=tf.float32)
    return x, y

path=".//dataset/"
box=os.listdir(path)
for b in box:
    f=open(path+b,"r",encoding='utf-8')
    r_tem=f.readlines()
    s=0
    for step in r_tem:
        if s==0:
            if box.index(b)==0 :
                val=[int(step.replace('\n',""))]
            else:
                val.append(int(step.replace('\n',"")))
        elif s==1:
            step=(step.replace(' \n',"")).split(" ")
            step=list(map(int, step))
            m_tem=[step]
        else:
            step=(step.replace(' \n',"")).split(" ")
            step=list(map(int,step))
            m_tem.append(step)
        s+=1
    if box.index(b)==0:
        dataset=[np.reshape(m_tem,(3,5,5))]
    else:
        dataset.append(np.reshape(m_tem,(3,5,5)))
val=tf.reshape(val,(len(val),1))
dataset=tf.data.Dataset.from_tensor_slices((val,dataset))
dataset=dataset.batch(1).map(preprocess).shuffle(50)


def main():
    conv_net.build(input_shape=[None, 5, 5, 3])
    conv_net.summary()
    fc_net.build(input_shape=[None, 500])
    optimizer = optimizers.Adam(lr=1e-4)
    variables = conv_net.trainable_variables + fc_net.trainable_variables

    conv_net.load_weights('.//conv_weight/')
    fc_net.load_weights('.//fc_weight/')
    for e in range(15):
        for step, (y, x) in enumerate(dataset):
            x = tf.reshape(x, [-1, 5, 5, 3])
            with tf.GradientTape() as tape:
                out = conv_net(x)
                out = tf.reshape(out, [-1,500])
                #print('out:',out)
                logit = fc_net(out)
               # print ('logit:',logit)
                y = tf.cast(y, dtype=tf.int32)
                y_onehot=tf.one_hot(y,depth=18)
                loss=tf.losses.categorical_crossentropy(y_onehot,logit,from_logits=True)
                loss = tf.reduce_mean(loss)
            grade=tape.gradient(loss,variables)
            optimizer.apply_gradients(zip(grade,variables))
            if step%10==0:
                print(step,"loss:",float(loss))
            conv_net.save_weights('.//conv_weight/')
            fc_net.save_weights('.//fc_weight/')
        print(e,'successfully save')

        total_num = 0
        total_correct = 0
        for step,(y,x) in enumerate(dataset):
            x = tf.reshape(x,[-1, 5, 5, 3])
            out = conv_net(x)
            out = tf.reshape(out, [-1, 500])
            logits = fc_net(out)
            # print('out:', out)
            prob = tf.nn.softmax(logits, axis=1)
            pred = tf.argmax(prob, axis=1)
            pred = tf.cast(pred, dtype=tf.float32)
            # print('pred:', pred)
            correct = tf.cast(tf.equal(pred, y), dtype=tf.int32)
            correct = tf.reduce_sum(correct)
            #print('correct:', correct)
            # 总的个位
            total_num += x.shape[0]
            # 预测正确的个数
            total_correct += int(correct)
        acc = total_correct / total_num
        print(e, 'acc:', acc)



if __name__ == '__main__':
    main()

