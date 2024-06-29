import subprocess

# 데이터를 로드하고 전처리
print("Running data_preprocessing.py...")
subprocess.run(["python", "data_preprocessing.py"])

# 모델을 정의하고 훈련
print("Running train_model.py...")
subprocess.run(["python", "train_model.py"])

# 모델을 평가
print("Running evaluate_model.py...")
subprocess.run(["python", "evaluate_model.py"])
