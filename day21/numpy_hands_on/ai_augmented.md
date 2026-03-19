## Prompt:-

Explain NumPy broadcasting and vectorisation in Python with simple practical examples. First define broadcasting and show how NumPy automatically expands arrays of different shapes during arithmetic operations. Then explain vectorisation and compare it with traditional Python loops using examples such as element-wise addition, multiplication, and array transformations. Include short code examples, output, and briefly explain why NumPy is faster and more memory-efficient than loops


## AI - Generated Output:-

### [ChatGPT Response](https://chatgpt.com/s/t_69bc230c1f788191b42e692e9b48694d)


### Are the examples correct?
Yes, the examples are correct because they follow NumPy rules for broadcasting and vectorised operations. In the broadcasting example, NumPy correctly expands the smaller array to match the larger array during addition. The vectorisation examples also produce correct element-wise results without using explicit loops. Each example clearly demonstrates the intended NumPy concept.

### Is the code efficient and runnable?
Yes, all code examples are runnable and efficient for basic array operations. NumPy performs calculations using optimized internal C routines, which makes execution faster than standard Python loops. Broadcasting also improves memory usage because NumPy avoids creating unnecessary copies of data. This makes the code suitable even for larger datasets.