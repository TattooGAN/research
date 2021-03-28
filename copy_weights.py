def copy_weights(model_source, model_target):
    # StyleVectorizer S
    model_target.GAN.S.load_state_dict(model_source.GAN.S.state_dict())

    # Generator G
    model_target.GAN.G.initial_conv.load_state_dict(model_source.GAN.G.initial_conv.state_dict())
    model_target.GAN.G.blocks[0].load_state_dict(model_source.GAN.G.blocks[0].state_dict())
    for i, block in enumerate(model_source.GAN.G.blocks[:0:-1]):
        model_target.GAN.G.blocks[len(model_target.GAN.G.blocks) - 1 - i].load_state_dict(block.state_dict())

    # StyleVectorizer  SE
    model_target.GAN.SE.load_state_dict(model_source.GAN.SE.state_dict())

    # Generator GE
    model_target.GAN.GE.initial_conv.load_state_dict(model_source.GAN.GE.initial_conv.state_dict())
    model_target.GAN.GE.blocks[0].load_state_dict(model_source.GAN.GE.blocks[0].state_dict())
    for i, block in enumerate(model_source.GAN.GE.blocks[:0:-1]):
        model_target.GAN.GE.blocks[len(model_target.GAN.GE.blocks) - 1 - i].load_state_dict(block.state_dict())

    # Discriminator    
    for i, block in enumerate(model_source.GAN.D.blocks):
        if i != len(model_source.GAN.D.blocks) - 1:
            model_target.GAN.D.blocks[i].load_state_dict(block.state_dict())
        else:
            model_target.GAN.D.blocks[-1].load_state_dict(block.state_dict())
    model_target.GAN.D.final_conv.load_state_dict(model_source.GAN.D.final_conv.state_dict())
    model_target.GAN.D.to_logit.load_state_dict(model_source.GAN.D.to_logit.state_dict())

    # Discriminator D_aug
    for i, block in enumerate(model_source.GAN.D_aug.D.blocks):
        if i != len(model_source.GAN.D_aug.D.blocks) - 1:
            model_target.GAN.D_aug.D.blocks[i].load_state_dict(block.state_dict())
        else:
            model_target.GAN.D_aug.D.blocks[-1].load_state_dict(block.state_dict())
    model_target.GAN.D_aug.D.final_conv.load_state_dict(model_source.GAN.D_aug.D.final_conv.state_dict())
    model_target.GAN.D_aug.D.to_logit.load_state_dict(model_source.GAN.D_aug.D.to_logit.state_dict())
