# ir_final

## preprocessing
- **function:** replace number and English in query, number replace with '\<num>', English replace with '\<English>', 
Url extract key word
- **input:** intput_filename output_filename keep-num keep-alpha keep-url
- **output:** void
- **bash:** python src/preprocessing.py -i data/2w_seg_data/user_tag_query.2W.seg.utf8.TRAIN -o data/processed/2w/2w.data.url.TRAIN --keep-url --keep-num

## feature extract
- **function:** gram=[1,2, ...] mode=['binary','tf','tfidf', 'idf'']
- **input:** input_filename, output_filename, gram=1, mode='tf', max_df=1.0, min_df=0.0, cf=1
- **output:** void
- **bash:** python src/feature_extract.py -i data/processed/2w/2w.data.TRAIN -o data/feature/2w/2w.1gram_idf_maxdf1.00_mindf0.00_cf1.Train -m idf

## classifier
- **function:** Generate a Classifier from arguments
- **input:** classifier=['NB', 'SGD']
- **sgd argument:** loss iter alpha shuffle

## feature selection
- **function:** filter=['DF',''IG','MI','Chi'] mode=['num','proportion']
- **input:** input_filename, output_filename, filter='MI', mode='proportion', num=0, proportion=1.0
- **output:** void

## model
- **function:** run cross validation
- **input:** x y classifier cv_num random
- **output:** score

## classifier
- **function:** Generate a SKlearn Classifier from args
- **input:** args
- **output:** classifier

## word_embedding
- **function:** Run Word Embedding Exp
- **input:** data embedding classifier pooling
- **output:** score

## run
- **function:** Run Traditional Feature Exp
- **input:** data classifier feature
- **output:** score

## multi process shell
- **function:** Run Bash File in Multi-Process
- **input:** bash_file, process_num
- **output:** void

## arguments
- **function:** Add arguments
- **input:** args
- **output:** void