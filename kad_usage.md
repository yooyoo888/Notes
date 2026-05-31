# Kernel Audio Distance Toolkit

[KAD toolkit](https://github.com/YoonjinXD/kadtk)


[paper link](https://arxiv.org/abs/2502.15602)

## 1. Installation
```Python >=3.9,<3.12```


I use Python 3.11.15


Requirement: torch and tensorflow>=2.0


```
pip install tensorflow[and-cuda]
pip install torch==2.1.2 torchvision==0.16.2 torchaudio==2.1.2 --index-url https://download.pytorch.org/whl/cu121
pip install kadtk
```

## 2. Usage

```kadtk {model_name} {reference-set dir} {target-set dir}```

```Python
import os
import subprocess
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
# 設定基準資料夾與輸出的 CSV 檔案名稱
baseline = "./D4_D7_tempo40_violin/"
csv_kad = "kad_v_results.csv"
csv_fad = "fad_v_results.csv"

# 在此列表中填寫所有需要計算的目標資料夾路徑
target_dirs = [
    'D4_D7_tempo40_violin',
    'D4_D7_tempo40_zitan',
    'D4_D7_tempo40_erhu_redwood',
    'D4_D7_tempo40_erhu_synthetic',
    'D4_D7_tempo40_piano',
    'D4_D7_tempo40_piano_m_piano_to_erhu_violin_0.3',
    'D4_D7_tempo40_piano_m_piano_to_erhu_violin_0.5',
    'D4_D7_tempo40_piano_m_piano_to_erhu_violin_0.7'
]

for target in target_dirs:
    print(f"正在處理目標資料夾: {target}")
    
    # 計算 KAD
    subprocess.run([
        "kadtk", "vggish", baseline, target, "--csv", csv_kad
    ], check=True)
    
    # 計算 FAD
    subprocess.run([
        "kadtk", "vggish", baseline, target, "--fad", "--csv", csv_fad
    ], check=True)
    
```

supported model list:  
>{clap-2023,clap-laion-audio,clap-laion-music,vggish,panns-cnn14-32k,panns-cnn14-16k,panns-wavegram-logmel,MERT-v1-95M-1,MERT-v1-95M-2,MERT-v1-95M-3,MERT-v1-95M-4,MERT-v1-95M-5,MERT-v1-95M-6,MERT-v1-95M-7,MERT-v1-95M-8,MERT-v1-95M-9,MERT-v1-95M-10,MERT-v1-95M-11,MERT-v1-95M,encodec-emb,encodec-emb-48k,dac-44kHz,cdpam-acoustic,cdpam-content,w2v2-base-1,w2v2-base-2,w2v2-base-3,w2v2-base-4,w2v2-base-5,w2v2-base-6,w2v2-base-7,w2v2-base-8,w2v2-base-9,w2v2-base-10,w2v2-base-11,w2v2-base,w2v2-large-1,w2v2-large-2,w2v2-large-3,w2v2-large-4,w2v2-large-5,w2v2-large-6,w2v2-large-7,w2v2-large-8,w2v2-large-9,w2v2-large-10,w2v2-large-11,w2v2-large-12,w2v2-large-13,w2v2-large-14,w2v2-large-15,w2v2-large-16,w2v2-large-17,w2v2-large-18,w2v2-large-19,w2v2-large-20,w2v2-large-21,w2v2-large-22,w2v2-large-23,w2v2-large,hubert-base-1,hubert-base-2,hubert-base-3,hubert-base-4,hubert-base-5,hubert-base-6,hubert-base-7,hubert-base-8,hubert-base-9,hubert-base-10,hubert-base-11,hubert-base,hubert-large-1,hubert-large-2,hubert-large-3,hubert-large-4,hubert-large-5,hubert-large-6,hubert-large-7,hubert-large-8,hubert-large-9,hubert-large-10,hubert-large-11,hubert-large-12,hubert-large-13,hubert-large-14,hubert-large-15,hubert-large-16,hubert-large-17,hubert-large-18,hubert-large-19,hubert-large-20,hubert-large-21,hubert-large-22,hubert-large-23,hubert-large,wavlm-base-1,wavlm-base-2,wavlm-base-3,wavlm-base-4,wavlm-base-5,wavlm-base-6,wavlm-base-7,wavlm-base-8,wavlm-base-9,wavlm-base-10,wavlm-base-11,wavlm-base,wavlm-base-plus-1,wavlm-base-plus-2,wavlm-base-plus-3,wavlm-base-plus-4,wavlm-base-plus-5,wavlm-base-plus-6,wavlm-base-plus-7,wavlm-base-plus-8,wavlm-base-plus-9,wavlm-base-plus-10,wavlm-base-plus-11,wavlm-base-plus,wavlm-large-1,wavlm-large-2,wavlm-large-3,wavlm-large-4,wavlm-large-5,wavlm-large-6,wavlm-large-7,wavlm-large-8,wavlm-large-9,wavlm-large-10,wavlm-large-11,wavlm-large-12,wavlm-large-13,wavlm-large-14,wavlm-large-15,wavlm-large-16,wavlm-large-17,wavlm-large-18,wavlm-large-19,wavlm-large-20,wavlm-large-21,wavlm-large-22,wavlm-large-23,wavlm-large,whisper-tiny,whisper-small,whisper-base,whisper-medium,whisper-large,openl3-mel256-env,openl3-mel256-music,openl3-mel128-env,openl3-mel128-music,passt-base-10s,passt-base-20s,passt-base-30s,passt-openmic,passt-fsd50k}