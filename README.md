
# Kidney-Disease-Classification-MLflow-DVC

May the data be with you 

# How to run?

### STEPS:
Clone the repository
```bash
https://github.com/Immortal-Pi/TumorFlow
```

### STEP 01- Create a conda environment after opening the repository
```bash 
conda create -n mlopscnn python=3.9 -y
```
```bash 
conda activate mlopscnn
```

### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```

# Finally run the following command
```bash
python main.py
```

Now,

open up you local host and port

# MLFLOW 

dagshub 

```bash
import dagshub
dagshub.init(repo_owner='Immortal-Pi', repo_name='TumorFlow', mlflow=True)
```

### DVC cmd 

1. dvc init 
2. dvc repro
3. dvc dag 