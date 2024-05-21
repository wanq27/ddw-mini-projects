// Transcrypt'ed from Python, 2023-09-24 22:44:39
var random = {};
import {AssertionError, AttributeError, BaseException, DeprecationWarning, Exception, IndexError, IterableError, KeyError, NotImplementedError, RuntimeWarning, StopIteration, UserWarning, ValueError, Warning, __JsIterator__, __PyIterator__, __Terminal__, __add__, __and__, __call__, __class__, __envir__, __eq__, __floordiv__, __ge__, __get__, __getcm__, __getitem__, __getslice__, __getsm__, __gt__, __i__, __iadd__, __iand__, __idiv__, __ijsmod__, __ilshift__, __imatmul__, __imod__, __imul__, __in__, __init__, __ior__, __ipow__, __irshift__, __isub__, __ixor__, __jsUsePyNext__, __jsmod__, __k__, __kwargtrans__, __le__, __lshift__, __lt__, __matmul__, __mergefields__, __mergekwargtrans__, __mod__, __mul__, __ne__, __neg__, __nest__, __or__, __pow__, __pragma__, __pyUseJsNext__, __rshift__, __setitem__, __setproperty__, __setslice__, __sort__, __specialattrib__, __sub__, __super__, __t__, __terminal__, __truediv__, __withblock__, __xor__, abs, all, any, assert, bool, bytearray, bytes, callable, chr, copy, deepcopy, delattr, dict, dir, divmod, enumerate, filter, float, getattr, hasattr, input, int, isinstance, issubclass, len, list, map, max, min, object, ord, pow, print, property, py_TypeError, py_iter, py_metatype, py_next, py_reversed, py_typeof, range, repr, round, set, setattr, sorted, str, sum, tuple, zip} from './org.transcrypt.__runtime__.js';
import * as __module_random__ from './random.js';
__nest__ (random, '', __module_random__);
var __name__ = '__main__';
export var gen_random_int = function (number, seed) {
	var numbers = list (range (number));
	random.seed (seed);
	random.shuffle (numbers);
	return numbers;
};
export var generate = function () {
	var number = 10;
	var seed = 200;
	var array = gen_random_int (number, seed);
	var array_str = ','.join (map (str, array)) + '.';
	document.getElementById ('generate').innerHTML = array_str;
	return array_str;
};
export var sortnumber1 = function (array_str) {
	var array_str = document.getElementById ('generate').innerHTML;
	var n = len (array_str);
	var array_ls = list (map (int, array_str.py_split (',')));
	var swapped = true;
	while (swapped) {
		var swapped = false;
		for (var i = 1; i < n; i++) {
			if (array_ls [i - 1] > array_ls [i]) {
				var __left0__ = tuple ([array_ls [i], array_ls [i - 1]]);
				array_ls [i - 1] = __left0__ [0];
				array_ls [i] = __left0__ [1];
				var swapped = true;
			}
		}
	}
	var array_str = ','.join (map (str, array_ls)) + '.';
	document.getElementById ('sorted').innerHTML = array_str;
	return array_str;
};
export var sortnumber2 = function () {
	var value = document.getElementsByName ('numbers') [0].value;
	if (value == '') {
		window.alert ('Your textbox is empty');
	}
	else {
		var array_ls = list (map (int, value.py_split (',')));
		var n = len (array_ls);
		var swapped = true;
		while (swapped) {
			var swapped = false;
			for (var i = 1; i < n; i++) {
				if (array_ls [i - 1] > array_ls [i]) {
					var __left0__ = tuple ([array_ls [i], array_ls [i - 1]]);
					array_ls [i - 1] = __left0__ [0];
					array_ls [i] = __left0__ [1];
					var swapped = true;
				}
			}
		}
		var array_str = ','.join (map (str, array_ls)) + '.';
	}
	print (array_str);
	document.getElementById ('sorted').innerHTML = array_str;
	return array_str;
};

//# sourceMappingURL=library.map