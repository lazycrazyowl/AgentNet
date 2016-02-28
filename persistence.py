import pickle,os
import lasagne
def save(nn,fname):
    param_list = lasagne.layers.get_all_params(nn)
    
    params = {par.name: par.get_value() for par in param_list}
    
    assert len(params) == len(param_list)#assert no duplicate layer names
    
    with open(fname,'w') as fout:
        pickle.dump(params,fout)
        
def load(nn,fname):
    param_containters = lasagne.layers.get_all_params(nn)
    
    with open(fname,'r') as fin:
        saved_params=pickle.load(fin)
    
    for param in param_containters:
        param.set_value(saved_params[param.name])
    return nn



