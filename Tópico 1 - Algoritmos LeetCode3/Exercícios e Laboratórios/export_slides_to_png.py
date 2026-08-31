import os
import fitz  # PyMuPDF

def export_pdf_pages_to_png(pdf_path, output_dir, scale=2.0):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir, exist_ok=True)

    doc = fitz.open(pdf_path)
    slide_names = [
        "slide_01_capa",
        "slide_02_relevancia_mercado",
        "slide_03_enunciado_problema",
        "slide_04_tres_abordagens_codigo",
        "slide_05_rastreio_passo_a_passo",
        "slide_06_benchmark_economia_cpu",
        "slide_07_diagrama_janela_deslizante",
        "slide_08_implementacao_c_ponteiros",
        "slide_09_tabela_complexidade_big_o",
        "slide_10_casos_de_borda_conclusao"
    ]

    print(f"Exportando {len(doc)} slides em alta resolução ({scale}x)...")

    # Zoom matrix for crisp HD output (2x scale = 2560x1440 resolution)
    mat = fitz.Matrix(scale, scale)

    generated_files = []
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        pix = page.get_pixmap(matrix=mat, alpha=False)
        
        name = slide_names[page_num] if page_num < len(slide_names) else f"slide_{page_num+1:02d}"
        output_file = os.path.join(output_dir, f"{name}.png")
        pix.save(output_file)
        generated_files.append(output_file)
        print(f"  -> Gerado: {output_file} ({pix.width}x{pix.height} px)")

    print(f"\nSucesso! {len(generated_files)} imagens PNG salvas em: {output_dir}")
    return generated_files

if __name__ == "__main__":
    pdf_file = "01_Apresentacao_e_Slides/Apresentacao_LeetCode3_Equipe_IFSP.pdf"
    if not os.path.exists(pdf_file):
        pdf_file = "Apresentacao_LeetCode3_Equipe_IFSP.pdf"
        
    out_dir_1 = "01_Apresentacao_e_Slides/imagens_png"
    out_dir_2 = "_Vault - Algoritmos/assets/imagens_slides"

    export_pdf_pages_to_png(pdf_file, out_dir_1, scale=2.0)
    export_pdf_pages_to_png(pdf_file, out_dir_2, scale=2.0)
