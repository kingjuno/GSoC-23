pip install -r requirements.txt
sudo /opt/conda/bin/jupyter nbconvert --execute notebooks/c8cnn/c8cnn-model1.ipynb --to notebook --inplace #TODO pass this as a argument
sudo /opt/conda/bin/jupyter notebook --ip='0.0.0.0' --allow-root