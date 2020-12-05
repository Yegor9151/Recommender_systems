import pandas as pd

def reduction_memory(df: pd.DataFrame) -> pd.DataFrame:
    """function for reduction memory size"""
    
    df_c = df.copy()
    
    for column in df_c.columns:
    
        series = df_c[df_c[column].notna()][column]
        
        if series.dtype == 'float64':
            if (series != series.astype('float32')).sum() == 0:
                df_c[column] = series.astype('float32')
        elif series.dtype == 'int64':
            if (series != series.astype('int8')).sum() == 0:
                df_c[column] = series.astype('int8')
            elif (series != series.astype('int16')).sum() == 0:
                df_c[column] = series.astype('int16')
            elif (series != series.astype('int32')).sum() == 0:
                df_c[column] = series.astype('int32')
                
    mb_before = df.memory_usage().sum() * 1e-6
    mb_after = df_c.memory_usage().sum() * 1e-6
    mb_reduced = mb_before - mb_after
    
    print(f'before:\t\t{round(mb_before, 2)} MB\n', 
          f'after:\t\t{round(mb_after, 2)} MB\n',
          f'reduсed:\t{round(mb_reduced, 2)} MB',
          sep='')
    
    return df_c
