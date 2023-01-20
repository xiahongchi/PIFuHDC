python -m apps.train_color \
    --dataroot ~/data/renderpeople/train/ \
    --num_sample_inout 0 --num_sample_color 5000 --sigma 0.1 --random_flip --random_scale --random_trans \
    --batch_size 1 \
    --load_netMR_checkpoint_path ./checkpoints/pifuhd.pt --load_netC_checkpoint_path ./checkpoints/net_C.pt