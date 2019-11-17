def zscore(data):

    x=64
    u=mean(data)
    sample_sd=samplestand(data)
    y=subtraction(x,u)
    return division(sample_sd,y)