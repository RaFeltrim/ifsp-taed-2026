// Partícula circular que se move, quica nas bordas e ricocheteia em outras partículas.

class Particle {
  constructor(id, x, y, vx, vy, r) {
    this.id = id; // índice único, usado para testar cada par uma só vez
    this.x = x;
    this.y = y;
    this.vx = vx; // velocidade em px por frame
    this.vy = vy;
    this.r = r;
    this.colliding = false;
    this.selected = false;
  }

  // Avança um frame. Ao passar de uma borda, encosta a partícula nela
  // e faz a velocidade apontar para dentro (quique).
  move(width, height) {
    this.x += this.vx;
    this.y += this.vy;

    if (this.x < this.r) {
      this.x = this.r;
      this.vx = Math.abs(this.vx);
    } else if (this.x > width - this.r) {
      this.x = width - this.r;
      this.vx = -Math.abs(this.vx);
    }

    if (this.y < this.r) {
      this.y = this.r;
      this.vy = Math.abs(this.vy);
    } else if (this.y > height - this.r) {
      this.y = height - this.r;
      this.vy = -Math.abs(this.vy);
    }
  }
}

// Dois círculos se sobrepõem quando a distância entre os centros é menor que a soma dos raios.
// Comparamos os quadrados para evitar a raiz quadrada.
function particlesOverlap(a, b) {
  const dx = b.x - a.x;
  const dy = b.y - a.y;
  const minDist = a.r + b.r;
  return dx * dx + dy * dy < minDist * minDist;
}

// Colisão elástica entre partículas de mesma massa.
function resolveCollision(a, b) {
  let dx = b.x - a.x;
  let dy = b.y - a.y;
  let dist = Math.hypot(dx, dy);

  // Centros no mesmo ponto: não há direção definida, escolhemos o eixo x.
  let nx = 1;
  let ny = 0;
  if (dist > 0) {
    nx = dx / dist;
    ny = dy / dist;
  }

  // 1) Separar: cada uma anda metade da sobreposição ao longo da normal.
  const overlap = a.r + b.r - dist;
  if (overlap > 0) {
    a.x -= nx * overlap / 2;
    a.y -= ny * overlap / 2;
    b.x += nx * overlap / 2;
    b.y += ny * overlap / 2;
  }

  // 2) Ricochetear: com massas iguais, basta trocar as componentes da
  // velocidade na direção da normal. Só faz isso se estão se aproximando.
  const approach = (a.vx - b.vx) * nx + (a.vy - b.vy) * ny;
  if (approach > 0) {
    a.vx -= approach * nx;
    a.vy -= approach * ny;
    b.vx += approach * nx;
    b.vy += approach * ny;
  }
}

// No Node (testes) exporta; no navegador os nomes acima já ficam globais.
if (typeof module !== 'undefined') module.exports = { Particle, particlesOverlap, resolveCollision };
