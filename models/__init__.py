'''
Initialize the models module
'''
from models.transformer import Transformer
from models.new_transformer import NewTransformer
from models.single_learned_pos_emb_transformer import SingleLearnedPosEmbTransformer
from models.multi_learned_pos_emb_transformer import MultiLearnedPosEmbTransformer
from models.interleave_learned_pos_emb_transformer import InterleaveLearnedPosEmbTransformer

MODELS = {
    'transformer': Transformer,
    'new_transformer': NewTransformer,
    'single_learned_pos_emb_transformer': SingleLearnedPosEmbTransformer,
    'multi_learned_pos_emb_transformer': MultiLearnedPosEmbTransformer,
    'interleave_learned_pos_emb_transformer': InterleaveLearnedPosEmbTransformer
}
