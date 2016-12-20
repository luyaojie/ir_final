# ir_final

## preprocessing
- **function:** replace number and English in query, number replace with '<num>', English replace with '<English>'
- **input:** intput_filename output_filename keep-num keep-alpha
- **output:** void

## feature structure
- **function:** gram=[1,2] mode=['binary','tf','tf-idf','doc2vec']
- **input:** input_filename, output_filename, gram=1, mode='tf'
- **output:** void

## feature selection
- **function:** filter=['DF',''IG','MI','Chi'] mode=['num','proportion']
- **input:** input_filename, output_filename, filter='MI', mode='proportion', num=0, proportion=1.0
- **output:** void

## model
- **function:** classifier=['NB','LR']
- **input:** train_data_x train_data_y test_data_x test_data_y classifier param
- **output:** score

## ensemble

