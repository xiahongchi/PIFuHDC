import torch
import argparse
    
if __name__ == '__main__':
    model = torch.load('../PIFu/checkpoints/net_C')
    # model = torch.load('color_train_models/train_all_netC/netC_latest')

    s_model = {}
    s_model['model_state_dict'] = {}
    for k, v in model.items():
        s_model['model_state_dict'][k] = v 
    
    
    
    parser = argparse.ArgumentParser(description='sort given numbers')
    parser.add_argument('--norm_color', type = str, default='group')
    parser.add_argument('--mlp_dim_color', type = list, default=[513, 1024, 512, 256, 128, 3])
    parser.add_argument('--mlp_res_layers_color', type = list, default=[])
    parser.add_argument('--use_tanh', action='store_true')
    parser.add_argument('--no_residual', action='store_true')
    parser.add_argument('--mlp_norm_color', type = str, default='group')
    parser.add_argument('--loadSize', type = int, default=512)
    parser.add_argument('--z_size', type = float, default=200.0)
    parser.add_argument('--color_loss_type', type = str, default='l1')
    opt = parser.parse_args()
    print(opt)

    
    s_model['opt'] = opt
    
    torch.save(s_model, 'checkpoints/net_C_nos2t.pt')
    # torch.save(s_model, 'checkpoints/net_C_finetune.pt')