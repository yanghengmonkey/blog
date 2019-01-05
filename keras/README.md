# KERAS
[Homepage]: https://keras.io/

## PREPROCESSING
* **Activations**
     + softmax
     ```
     keras.activations.softmax(x, axis=-1)
     ```
     + elu
     ```
     keras.activations.elu(x, alpha=1.0)
     ```
     + relu
     ```
     keras.activations.relu(
         x, 
         alpha=0.0, 
         max_value=None, 
         threshold=0.0
         )
     ```
* **Losses**
    + categorical_crossentropy
    ```
    keras.losses.categorical_crossentropy(
        y_true, 
        y_pred
        )
    ```
### Datasets
* CIFAR10 small image classification
* CIFAR100 small image classification
* Reuters newswire topics classification
* MNIST database of handwritten digits
* Fashion-MNIST database of fashion articles
* Boston housing price regression dataset
## MODELS
* Sequential model
    - model.layers
    - model.inputs
    - model.outputs
    - model.summary()
    - model.get_config()
    - model.set_weights(weights)
    - model.to_json()
    - model.to_yaml()
    - model.get_weights()
    - model.save_weights(filepath)
    - model.load_weights(filepath, by_name=False)
* Model(functional API)
## LAYERS
* **common methods**
    + Common
        - layer.get_weights()
        - layer.set_weights(weights)
        - layer.get_config()
    + If has a signal node
        - layer.input
        - layer.input_shape
        - layer.output
        - layer.output_shape
    + If has multiple nodes 
        - layer.get_input_at( node_index )
        - layer.get_input_shape_at( node_index )
        - layer.get_output_at( node_index )
        - layer.get_output_shape_at( node_index )
* **Core Layers**
    + Dense
      ```
      keras.layers.Dense(
          units, 
          activation=None, 
          use_bias=True, 
          kernel_initializer='glorot_uniform', 
          bias_initializer='zeros', 
          kernel_regularizer=None, 
          bias_regularizer=None, 
          activity_regularizer=None, 
          kernel_constraint=None, 
          bias_constraint=None
      )
      ```
    + Activation
      ```
      keras.layers.Activation(activation)
      ```
    + Flatten
      ```
      keras.layers.Flatten(data_format=None)
      ```
    + Input
      ```
      keras.engine.input_layer.Input()
      ```
    + Reshape
      ```
      keras.layers.Reshape(target_shape)
      ```
    + Permute
      ```
      keras.layers.Permute(dims)
      ```
* **COnvolutional Layers**
    + Conv1D
    ```
    keras.layers.Conv1D(
        filters, 
        kernel_size, 
        strides=1, 
        padding='valid', 
        data_format='channels_last', 
        dilation_rate=1, 
        activation=None, 
        use_bias=True, 
        kernel_initializer='glorot_uniform', 
        bias_initializer='zeros', 
        kernel_regularizer=None, 
        bias_regularizer=None, 
        activity_regularizer=None, 
        kernel_constraint=None, 
        bias_constraint=None
        )
    ```
    + Conv2D
    ```
    keras.layers.Conv2D(
        filters, 
        kernel_size, 
        strides=(1, 1), 
        padding='valid', 
        data_format=None, 
        dilation_rate=(1, 1), 
        activation=None, 
        use_bias=True, 
        kernel_initializer='glorot_uniform', 
        bias_initializer='zeros', 
        kernel_regularizer=None, 
        bias_regularizer=None, 
        activity_regularizer=None, 
        kernel_constraint=None, 
        bias_constraint=None
        )
    ```
    + SeparableConv1D
    ```
    ```
    + SeparableConv2D
    ```
    ```
    + DepthwiseConv2D
    ```
    ```
    + Conv2DTranspose
    ```
    ```
    + Conv3D
    ```
    ```
    + Conv3DTranspose
    ```
    ```
    + Cropping1D
    ```
    ```
    + Cropping2D
    ```
    ```
    + Cropping3D
    ```
    ```
    + UpSampling1D
    ```
    ```
    + UpSampling2D
    ```
    ```
    + UpSampling3D
    ```
    ```
    + ZeroPadding1D
    ```
    ```
    + ZeroPadding2D
    ```
    ```
    + ZeroPadding3D
    ```
    ```
* **Pooling Layers**
    + MaxPooling1D
    ```
    keras.layers.MaxPooling1D(
        pool_size=2, 
        strides=None, 
        padding='valid', 
        data_format='channels_last'
        )
    ```
    + MaxPooling2D
    ```
    keras.layers.MaxPooling2D(
        pool_size=(2, 2), 
        strides=None, 
        padding='valid', 
        data_format=None
        )
    ```
    + MaxPooling3D
    ```
    keras.layers.MaxPooling3D(
        pool_size=(2, 2, 2), 
        strides=None, 
        padding='valid', 
        data_format=None
        )
    ```
    + AveragePooling1D
    ```
    keras.layers.AveragePooling1D(
        pool_size=2, 
        strides=None, padding='valid', data_format='channels_last')
    ```
### Utils
    + to_categorical
    ```
    keras.utils.to_categorical(
         y, 
         num_classes=None, 
         dtype='float32'
         )
    ```

