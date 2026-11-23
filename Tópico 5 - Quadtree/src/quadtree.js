// Quadtree de pontos: divide o espaço em 4 quadrantes sempre que um nó fica cheio.

// Retângulo alinhado aos eixos: (x, y) é o canto superior esquerdo.
class Rect {
  constructor(x, y, w, h) {
    this.x = x;
    this.y = y;
    this.w = w;
    this.h = h;
  }

  // Borda direita/inferior exclusiva: um ponto na divisa cai em um único quadrante.
  contains(px, py) {
    return px >= this.x && px < this.x + this.w &&
           py >= this.y && py < this.y + this.h;
  }

  intersects(other) {
    return other.x < this.x + this.w && other.x + other.w > this.x &&
           other.y < this.y + this.h && other.y + other.h > this.y;
  }
}

class Quadtree {
  constructor(boundary, capacity = 4, depth = 0, maxDepth = 8) {
    this.boundary = boundary;
    this.capacity = capacity; // itens que cabem no nó antes de subdividir
    this.depth = depth;
    this.maxDepth = maxDepth; // limite que evita subdivisão infinita
    this.items = [];
    this.children = null; // null enquanto o nó é folha
  }

  // Insere um item com { x, y }. Retorna false se o ponto está fora deste nó.
  insert(item) {
    if (!this.boundary.contains(item.x, item.y)) return false;

    if (this.children === null) {
      // Folha: guarda aqui se ainda há espaço ou se já chegamos na profundidade máxima.
      if (this.items.length < this.capacity || this.depth === this.maxDepth) {
        this.items.push(item);
        return true;
      }
      this.subdivide();
    }

    return this.insertIntoChild(item);
  }

  // Cria os 4 quadrantes e redistribui os itens que estavam neste nó.
  subdivide() {
    const { x, y, w, h } = this.boundary;
    const hw = w / 2;
    const hh = h / 2;
    const d = this.depth + 1;
    this.children = [
      new Quadtree(new Rect(x + hw, y, hw, hh), this.capacity, d, this.maxDepth),      // NE
      new Quadtree(new Rect(x, y, hw, hh), this.capacity, d, this.maxDepth),           // NW
      new Quadtree(new Rect(x + hw, y + hh, hw, hh), this.capacity, d, this.maxDepth), // SE
      new Quadtree(new Rect(x, y + hh, hw, hh), this.capacity, d, this.maxDepth),      // SW
    ];

    for (const item of this.items) this.insertIntoChild(item);
    this.items = [];
  }

  insertIntoChild(item) {
    for (const child of this.children) {
      if (child.insert(item)) return true;
    }
    return false;
  }

  // Range query: devolve os itens cujo ponto está dentro de `range`.
  // Nós que não tocam o range são descartados inteiros: é isso que torna a busca rápida.
  // Se `visited` for passado, registra o caminho para o modo didático: cada nó visitado,
  // se ele tocou o range (`hit`) e os itens que achou nele (`found`). Sem ele, nada muda.
  query(range, found = [], visited = null) {
    const hit = this.boundary.intersects(range);
    const record = visited ? { node: this, hit, found: [] } : null;
    if (record) visited.push(record);
    if (!hit) return found;

    for (const item of this.items) {
      if (range.contains(item.x, item.y)) {
        found.push(item);
        if (record) record.found.push(item);
      }
    }
    if (this.children !== null) {
      for (const child of this.children) child.query(range, found, visited);
    }
    return found;
  }
}

// No Node (testes) exporta; no navegador os nomes acima já ficam globais.
if (typeof module !== 'undefined') module.exports = { Rect, Quadtree };
