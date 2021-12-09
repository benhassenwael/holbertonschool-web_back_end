export default function createIteratorObject(report) {
  const allEmp = Object.values(report.allEmployees).flat();
  return {
    [Symbol.iterator]() {
      let current = 0;
      const last = allEmp.length;
      return {
        next() {
          if (current < last) {
            const ret = { done: false, value: allEmp[current], delim: ' | ' };
            current += 1;
            if (!(current < last)) ret.delim = '';
            return ret;
          }
          return { done: true, value: undefined };
        },
      };
    },
  };
}
