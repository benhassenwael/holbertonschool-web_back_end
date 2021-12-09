export default function iterateThroughObject(reportWithIterator) {
  let txt = '';
  const iter = reportWithIterator[Symbol.iterator]();

  for (let res = iter.next(); !res.done; res = iter.next()) {
    txt += res.value + res.delim;
  }

  return txt;
}
