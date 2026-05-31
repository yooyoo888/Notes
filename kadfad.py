import os
import subprocess
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
# 設定基準資料夾與輸出的 CSV 檔案名稱
baseline = "./D4_D7_tempo40_erhu_redwood/"
csv_kad = "kad_results.csv"
csv_fad = "fad_results.csv"

# 在此列表中填寫所有需要計算的目標資料夾路徑
target_dirs = [
    'D4_D7_tempo40_erhu_redwood',
    'D4_D7_tempo40_violin',
    'D4_D7_tempo40_zitan',
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
    
