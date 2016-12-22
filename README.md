# ir_final

## preprocessing
- **function:** replace number and English in query, number replace with '\<num>', English replace with '\<English>', 
Url extract key word
- **input:** intput_filename output_filename keep-num keep-alpha keep-url
- **output:** void

## feature extract
- **function:** gram=[1,2] mode=['binary','tf','tfidf', 'idf'']
- **input:** input_filename, output_filename, gram=1, mode='tf', max_df=1.0, min_df=0.0, cf=1
- **output:** void

## feature selection
- **function:** filter=['DF',''IG','MI','Chi'] mode=['num','proportion']
- **input:** input_filename, output_filename, filter='MI', mode='proportion', num=0, proportion=1.0
- **output:** void

## model
- **function:** classifier=['NB','LR', 'SGD']
- **input:** train_data_x train_data_y test_data_x test_data_y classifier param
- **output:** score

## ensemble

