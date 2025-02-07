import pandas as pd
import numpy as np


# np.random.seed(42)
# df = pd.DataFrame({
#     'id': np.arange(1, 1_000_001),
#     'value': np.random.randint(1, 100, size=1_000_000),
#     'category': np.random.choice(['A', 'B', 'C', 'D'], size=1_000_000),
#     'flag': np.random.choice([True, False], size=1_000_000)
# })

# # Before optimization
# print('Before oprimization')
# print(df.info(memory_usage='deep'))

# #Optimization
# df['id'] = df['id'].astype('int32')
# df['value'] = df['value'].astype('int8')
# df['category'] = df['category'].astype('category')
# df['flag'] = df['flag'].astype('uint8')

# #After optimization
# print('After optimization')
# print(df.info(memory_usage='deep'))



############################################




df = pd.DataFrame({
    'user_id': np.arange(1, 100_001),
    'salary': np.random.randint(20_000, 200_000, size=100_000),
    'department': np.random.choice(['IT', 'HR', 'Finance', 'Marketing'], size=100_000),
    'is_manager': np.random.choice([True, False], size=100_000)
})

# Check memory
print(df.info(memory_usage='deep'))


# Optimization
df['user_id'] = df['user_id'].astype('int16')
df['salary'] = df['salary'].astype('int16')
df['department'] = df['department'].astype('category')
df['is_manager'] = df['is_manager'].astype('uint8')

# After oprimization
print(df.info(memory_usage='deep'))