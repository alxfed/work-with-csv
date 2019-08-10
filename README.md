# work-with-csv
A bag of useful 'lower level' tricks
</br></br>
If you are processing 'raw' human input, that is "contained" (and I'm not using this word by accident) in a csv, you will have trouble with libraries like Pandas converting what's in it automatically. You need to go down a level and use the __csv__ library that doesn't interpret the contence of the csv that it reads. You may be sure that everything is delivered to you as strings and deal with it yourself.
