'''
Initialize the models module
'''
from models.transformer import Transformer
from models.new_transformer import NewTransformer
from models.single_learned_pos_emb_transformer import SingleLearnedPosEmbTransformer
from models.multi_learned_pos_emb_transformer import MultiLearnedPosEmbTransformer
from models.interleave_learned_pos_emb_transformer import InterleaveLearnedPosEmbTransformer
from models.multi_learned_pos_emb_encoder_only_transformer import MultiLearnedPosEmbEncOnlyTransformer
from models.interleave_learned_pos_emb_encoder_only_transformer import InterleaveLearnedPosEmbEncoderOnlyTransformer
from models.interleave_fixed_pos_emb_encoder_only_transformer import InterleaveFixedPosEmbEncoderOnlyTransformer
from models.sandwiched_fixed_pos_emb_encoder_only_transformer import SandwichedFixedPosEmbEncoderOnlyTransformer
from models.multi_fixed_pos_emb_encoder_only_transformer import MultiFixedPosEmbEncoderOnlyTransformer

MODELS = {
    'transformer': Transformer,
    'new_transformer': NewTransformer,
    'single_learned_pos_emb_transformer': SingleLearnedPosEmbTransformer,
    'multi_learned_pos_emb_transformer': MultiLearnedPosEmbTransformer,
    'interleave_learned_pos_emb_transformer': InterleaveLearnedPosEmbTransformer,
    # Multiple embeddings applied on encoder only models
    'multi_learned_pos_emb_encoder_only_transformer': MultiLearnedPosEmbEncOnlyTransformer,
    'interleave_learned_pos_emb_encoder_only_transformer': InterleaveLearnedPosEmbEncoderOnlyTransformer,
    'interleave_fixed_pos_emb_encoder_only_transformer': InterleaveFixedPosEmbEncoderOnlyTransformer,
    'sandwiched_fixed_pos_emb_encoder_only_transformer': SandwichedFixedPosEmbEncoderOnlyTransformer,
    'multi_fixed_pos_emb_encoder_only_transformer': MultiFixedPosEmbEncoderOnlyTransformer 
}
