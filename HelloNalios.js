let dict = 
{
  H : 72,
  e : 101,
  l : 108,
  o : 111,
  N : 78,
  a : 97,
  i : 105,
  s : 115,
  space : 32,
  comma : 44,
  exclamationPoint : 33,
};

function HelloNalios()
{
  console.log(String.fromCharCode(dict.H) + String.fromCharCode(dict.e) +
  String.fromCharCode(dict.l) + String.fromCharCode(dict.l) +
  String.fromCharCode(dict.o) + String.fromCharCode(dict.comma) +
  String.fromCharCode(dict.space) +
  String.fromCharCode(dict.N) + String.fromCharCode(dict.a) +
  String.fromCharCode(dict.l) + String.fromCharCode(dict.i) +
  String.fromCharCode(dict.o) + String.fromCharCode(dict.s) +
  String.fromCharCode(dict.space) + String.fromCharCode(dict.exclamationPoint));
}

HelloNalios();
