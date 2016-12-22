python src/feature_extract.py -i data/processed/2w/2w.data.TRAIN -o data/feature/2w/2w.1gram_binary_maxdf1.00_mindf0.00_cf1.Train -m binary
python src/feature_extract.py -i data/processed/10w/10w.data.TRAIN -o data/feature/10w/10w.1gram_binary_maxdf1.00_mindf0.00_cf1.Train -m binary

python src/feature_extract.py -i data/processed/2w/2w.data.TRAIN -o data/feature/2w/2w.1gram_tf_maxdf1.00_mindf0.00_cf1.Train -m tf
python src/feature_extract.py -i data/processed/10w/10w.data.TRAIN -o data/feature/10w/10w.1gram_tf_maxdf1.00_mindf0.00_cf1.Train -m tf

python src/feature_extract.py -i data/processed/2w/2w.data.TRAIN -o data/feature/2w/2w.1gram_idf_maxdf1.00_mindf0.00_cf1.Train -m idf
python src/feature_extract.py -i data/processed/10w/10w.data.TRAIN -o data/feature/10w/10w.1gram_idf_maxdf1.00_mindf0.00_cf1.Train -m idf

python src/feature_extract.py -i data/processed/2w/2w.data.TRAIN -o data/feature/2w/2w.1gram_tfidf_maxdf1.00_mindf0.00_cf1.Train -m tfidf
python src/feature_extract.py -i data/processed/10w/10w.data.TRAIN -o data/feature/10w/10w.1gram_tfidf_maxdf1.00_mindf0.00_cf1.Train -m tfidf
