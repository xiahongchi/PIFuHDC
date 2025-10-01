# Installation Guide for Windows (PIFuHDC)

This guide describes how to install and run the PIFuHDC project on **Windows 10/11** using **Anaconda** and the official **OpenPose binaries**. It is based on a verified working configuration from June 2025.

> 📌 For Linux/macOS users, see the original installation instructions in the [main README](../README.md).

> 🪟 For Windows users, you can now follow this fully working guide!

---

## ✅ Prerequisites

- [Anaconda](https://www.anaconda.com/products/distribution)
- [Git for Windows](https://git-scm.com/)
- [OpenPose v1.7.0 Windows release](https://github.com/CMU-Perceptual-Computing-Lab/openpose/releases)

---

## 🧪 Create the Python Environment

```bash
conda create -n pifuhdc python=3.6
conda activate pifuhdc
```

---

## 📥 Clone and Configure PIFuHDC

```bash
cd C:\
git clone https://github.com/xiahongchi/PIFuHDC
cd C:\PIFuHDC
```

### 🔧 Modify `requirements.txt`

Edit `PIFuHDC\requirements.txt`:

```diff
- opencv-python         # cv2
+ opencv-python==4.5.5.62
```

### 🔧 Modify `apps\batch_openpose.py`

Replace the command section with Windows-compatible code:

```python
input_path = os.path.abspath(args.input_root)
out_json_path = os.path.abspath(args.out_path)

os.makedirs(out_json_path, exist_ok=True)
exe_path = os.path.join(op_dir, "bin", "OpenPoseDemo.exe")
import subprocess

cmd = [
    exe_path,
    "--image_dir", input_path,
    "--write_json", out_json_path,
    "--render_pose", "0",
    "--display", "0",
    "--face_render", "0",
    "--hand_render", "0"
]
print("Running command:")
print(" ".join(cmd))
subprocess.run(cmd, check=True, cwd=op_dir)
```

### 🔧 Fix OpenGL GLUT window bug

In `lib\render\gl\render.py`, replace:

```python
glutCreateWindow("My Render.")
```

with:

```python
glutCreateWindow(b"My Render.")
```

### 🔧 Fix `rm` command in `apps\render_turntable.py`

Replace:

```python
cmd = 'rm %s/rot_*.png' % obj_root
os.system(cmd)
```

with:

```python
import glob
for f in glob.glob(os.path.join(obj_root, 'rot_*.png')):
    try:
        os.remove(f)
    except Exception as e:
        print(f"Error while deleting {f}: {e}")
```

---

## 📦 Install dependencies

```bash
pip install -r requirements.txt
```

---

## 📁 Download Pretrained Models

1. Download:

   - [https://dl.fbaipublicfiles.com/pifuhd/checkpoints/pifuhd.pt](https://dl.fbaipublicfiles.com/pifuhd/checkpoints/pifuhd.pt)
   - [https://drive.google.com/file/d/1jSOpwJKFJWHxkCEplhz0AUGacQBIS4AM](https://drive.google.com/file/d/1jSOpwJKFJWHxkCEplhz0AUGacQBIS4AM)

2. Move both files into:

```plaintext
PIFuHDC\checkpoints\
```

3. Rename:

```plaintext
net_C_HD.pt -> net_C_choice2.pt
```

---

## 🧍 Prepare Input

1. Create:

```plaintext
PIFuHDC\sample_images\
```

2. Copy PNG files (e.g. `test.png`) into that folder.
3. Image should be around 512x512.

---

## 📦 Install OpenPose

Download and extract:

- [OpenPose v1.7.0 Windows binaries (GPU)](https://github.com/CMU-Perceptual-Computing-Lab/openpose/releases/download/v1.7.0/openpose-1.7.0-binaries-win64-gpu-python3.7-flir-3d_recommended.zip)

Extract to:

```plaintext
C:\tools\openpose\
```

Make sure this exists:

```plaintext
C:\tools\openpose\bin\OpenPoseDemo.exe
```

Also make sure the `models\pose\body_25\` folder contains the required `.caffemodel` and `.prototxt`.

---

## 🚀 Run

### 1. Generate keypoints using OpenPose:

```bash
python apps/batch_openpose.py -d C:\tools\openpose -i sample_images -o sample_images
```

### 2. Run PIFuHDC inference:

```bash
python -m apps.test_colorHD --input_path sample_images --out_path results --ckpt_path checkpoints/pifuhd.pt --ckpt_path_Color checkpoints/net_C_choice2.pt
```

### 3. Render turntable video:

```bash
python -m apps.render_turntable -f results/pifuhd_final/recon
```

---

## ✅ Output

- `.obj` and `.mtl` models in `results/pifuhd_final/recon`
- `.mp4` rotation videos rendered using OpenGL and ffmpeg

---

## 🙌 Notes

- This guide was tested in a clean Windows 10 x64 system (Anaconda, CUDA-enabled GPU)
- Feel free to contribute back improvements or create a PR
- Windows installation reference has been added to the main [README](./README.md)

---

**Enjoy using PIFuHDC on Windows!**

