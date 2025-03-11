# NVIDIA Sionna: An Open-Source Library for 6G Physical-Layer Research

## 概述

Sionna是由NVIDIA開發的開源通訊函式庫，專為下一代無線通訊系統的研究與設計打造而成。它整合了通訊系統與深度學習模組，使研究人員能夠輕鬆設計、測試以及最佳化通訊系統。

## 核心特色

### 基於TensorFlow的架構

Sionna建立在TensorFlow之上，具有以下優勢：
- 原生GPU加速
- 平行化的模擬能力
- 與深度學習框架之整合

### Link Level通訊系統設計

Sionna支援完整通訊的建模與模擬：
- 訊號源編碼/解碼
- 調變/解調
- 通道編碼/解碼
- 通道估測

### 高自由度

- 模組化功能設計
- 支援使用者自定義模型



## 實際應用範例

### 範例一：Link Level通訊模擬
下圖為一個簡單的通訊系統模擬架構，
![sionna_simulate_basic_encode](fig/sionna_simulate_basic_encode.png)

### 範例二：





setup:
windows
到BIOS打開虛擬化
安裝WSL
安裝WSL的ubuntu
(ubuntu的資料夾路徑在檔案總管的網路的位置)
sudo apt update && sudo apt upgrade -y
sudo apt install llvm
下載&安裝conda
建立虛擬環境
```
pip install sionna
pip install jupyter notebook
conda install -c conda-forge libstdcxx-ng
```
find /usr/lib /usr/local/lib -name "libLLVM.so*"
export DRJIT_LIBLLVM_PATH=/usr/lib/llvm-14/lib/libLLVM.so




Reference
* NVIDIA website: https://developer.nvidia.com/sionna
* Sionna tutorial: https://nvlabs.github.io/sionna/index.html
* Sionna GitHub: https://github.com/NVlabs/sionna
