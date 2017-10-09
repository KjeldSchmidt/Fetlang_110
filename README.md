# Fetlang_110

This repository provides proof of [Fetlangs](https://github.com/Property404/fetlang) Turing Completeness by implementing [Rule 110](https://en.wikipedia.org/wiki/Rule_110) in Fetlang.

To build and try it yourself, check install instructions on Fetlangs github page.

I've neglected to add comand line parameters, so different starting configurations can only be tested by changing the source code. Sorry about that.
Valid input must begin and end with an #-symbol. For the non-generated version, the input string has to be 10 characters long (counting the #'s), for the generated, you have to set iteration accordingly.

To use the generated version, simply change the VARs and the input string ( 'Make Julia moan "#' + "0" * (gridWidth-3) + '1#"' ) and run it (with python 3, obviously)

Then you'll have to compile the generated file manually, as this effort is too small to warrant a fully automated build.




