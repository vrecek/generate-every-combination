# Generate every possible combination
Generate every possible combination of a characters, using this python script

### Usage
`python3 generate.py <min> <max> <arr> <?filename>`

### Arguments
`min` Minimum length of a generated word <br>
`max` Maximum length of a generated word <br>
`arr` Array of characters <br>
`filename` Optional filename. Default is **combinations**

### `arr` option
- `alpha_low` Lowercase alphanumeric <br>
- `alpha_upp` Uppercase alphanumeric <br>
- `numeric` Only numbers <br> <br>

You can either specify your own array. <br>
Characters must be comma separated <br>
For example: **a,b,c,d**, **b,5,f,0,s,l**

### Output
Generated files will be in a **combinations/** directory <br> <br>

### Example usage
`python3 generate.py 1 2 a,b` <br> <br>

Output:
```
a
b
aa
ab
ba
bb
```

<br> <br>

*** Be aware of performance issues while trying to generate a lot of combinations ***