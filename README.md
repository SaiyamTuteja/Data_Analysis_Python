
## 🔶 Part 1: Pandas Kya Hai?

**Pandas** ek Python ka library hai jo use hoti hai **data analysis** aur **data manipulation** ke liye. Isse tu data ko easily read, clean, modify aur analyze kar sakta hai.

> Soch: Excel jaisa sheet system, lekin programming ke zariye control.

---

## 🔶 Part 2: Basic Concepts

Pandas ke 2 main structure hote hain:

### 1. **Series**

* One-dimensional data (ek column)
* Jaise: list ya ek Excel ka column

```python
import pandas as pd

data = pd.Series([10, 20, 30, 40])
print(data)
```

### 2. **DataFrame**

* Two-dimensional (rows + columns)
* Jaise: Excel table

```python
data = {
    'Name': ['Ali', 'Sara', 'Ahmed'],
    'Age': [25, 30, 22]
}
df = pd.DataFrame(data)
print(df)
```

---

## 🔶 Part 3: Data Analysis ke Steps using Pandas

### ✅ Step 1: Pandas Install Karna

```bash
pip install pandas
```

### ✅ Step 2: Data Load Karna

```python
import pandas as pd

df = pd.read_csv('filename.csv')  # Excel ka CSV file
```

### ✅ Step 3: Data Ka Preview Lena

```python
df.head()       # Top 5 rows
df.tail()       # Last 5 rows
df.shape        # Rows x Columns
df.info()       # Data types aur null values
df.describe()   # Numeric summary (mean, std, min, etc.)
```

---

## 🔶 Part 4: Common Data Analysis Tasks

### 🔹 Columns Ko Dekhna

```python
df.columns
```

### 🔹 Specific Column

```python
df['Name']
```

### 🔹 Filtering Rows (Condition)

```python
df[df['Age'] > 25]  # Age > 25 wale log
```

### 🔹 Missing Values Handle Karna

```python
df.isnull().sum()       # Kitne null hain
df.dropna()             # Null hata do
df.fillna(0)            # Null ko 0 se bhardo
```

### 🔹 New Column Banana

```python
df['Age_plus_5'] = df['Age'] + 5
```

### 🔹 Grouping

```python
df.groupby('Gender')['Age'].mean()
```

### 🔹 Sorting

```python
df.sort_values(by='Age', ascending=False)
```

### 🔹 Export to CSV

```python
df.to_csv('newfile.csv', index=False)
```

---

## 🔶 Part 5: Visualization (Bonus with Matplotlib)

```python
import matplotlib.pyplot as plt

df['Age'].hist()
plt.show()
```

---

## ✅ Real World Flow Summary:

1. **CSV read karo**
2. **Preview karo (head, info)**
3. **Data clean karo (nulls, dtypes)**
4. **Filter, sort, modify**
5. **Group, summarize**
6. **Export ya visualize karo**

