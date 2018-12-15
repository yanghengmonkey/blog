# KERAS
[Homepage]: https://keras.io/

## PREPROCESSING
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
