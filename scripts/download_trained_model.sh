# Copyright (c) Facebook, Inc. and its affiliates. All rights reserved.

set -ex

mkdir -p checkpoints
cd checkpoints
wget "https://dl.fbaipublicfiles.com/pifuhd/checkpoints/pifuhd.pt" pifuhd.pt
wget "https://drive.google.com/file/d/1jSOpwJKFJWHxkCEplhz0AUGacQBIS4AM/view?usp=sharing" net_C_HD.pt
cd ..
