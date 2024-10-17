import os
import re
from typing import List, Tuple

class FNCConverter:
    def __init__(self):
        # Mapeamento de operadores
        self.operators = {
            '\\land': ('AND', '∧'),
            '\\lor': ('OR', '∨'),
            '\\lnot': ('NOT', '¬'),
            '\\rightarrow': ('IMPLIES', '→'),
            '\\leftrightarrow': ('IFF', '↔')
        }
        
        # Cores para o terminal
        self.colors = {
            'BLUE': '\033[94m',
            'GREEN': '\033[92m',
            'YELLOW': '\033[93m',
            'RED': '\033[91m',
            'BOLD': '\033[1m',
            'UNDERLINE': '\033[4m',
            'END': '\033[0m'
        }
    
    def parse_latex(self, formula: str) -> str:
        """Converte a fórmula LaTeX em uma representação interna."""
        result = formula.strip()
        for latex_op, (internal_op, _) in self.operators.items():
            result = result.replace(latex_op, internal_op)
        return result
    
    def to_latex(self, formula: str) -> str:
        """Converte a representação interna para LaTeX."""
        result = formula
        for latex_op, (internal_op, _) in self.operators.items():
            result = result.replace(internal_op, latex_op)
        return result
    
    def to_unicode(self, formula: str) -> str:
        """Converte a fórmula LaTeX para símbolos Unicode."""
        result = formula
        for latex_op, (_, unicode_op) in self.operators.items():
            result = result.replace(latex_op, unicode_op)
        return result

    def eliminate_iff(self, formula: str) -> str:
        """Elimina equivalências (IFF)."""
        while 'IFF' in formula:
            pattern = r'([^()]+)\s*IFF\s*([^()]+)'
            match = re.search(pattern, formula)
            if match:
                p, q = match.groups()
                replacement = f"(({p} IMPLIES {q}) AND ({q} IMPLIES {p}))"
                formula = formula.replace(match.group(0), replacement)
        return formula
    
    def eliminate_implies(self, formula: str) -> str:
        """Elimina implicações."""
        while 'IMPLIES' in formula:
            pattern = r'([^()]+)\s*IMPLIES\s*([^()]+)'
            match = re.search(pattern, formula)
            if match:
                p, q = match.groups()
                replacement = f"(NOT {p} OR {q})"
                formula = formula.replace(match.group(0), replacement)
        return formula
    
    def apply_de_morgan(self, formula: str) -> str:
        """Aplica as leis de De Morgan."""
        while 'NOT (' in formula:
            pattern = r'NOT \(([^()]+)\)'
            match = re.search(pattern, formula)
            if match:
                expr = match.group(1)
                if 'AND' in expr:
                    parts = expr.split('AND')
                    new_parts = [f"NOT {p.strip()}" for p in parts]
                    replacement = f"({' OR '.join(new_parts)})"
                elif 'OR' in expr:
                    parts = expr.split('OR')
                    new_parts = [f"NOT {p.strip()}" for p in parts]
                    replacement = f"({' AND '.join(new_parts)})"
                else:
                    replacement = expr
                formula = formula.replace(match.group(0), replacement)
        return formula
    
    def distribute_or(self, formula: str) -> str:
        """Aplica a distributividade do OR sobre AND."""
        while True:
            pattern = r'\(([^()]+)\s*OR\s*\(([^()]+\s*AND\s*[^()]+)\)\)'
            match = re.search(pattern, formula)
            if not match:
                pattern = r'\(\(([^()]+\s*AND\s*[^()]+)\)\s*OR\s*([^()]+)\)'
                match = re.search(pattern, formula)
            
            if match:
                p, qr = match.groups()
                q, r = qr.split('AND')
                replacement = f"(({p.strip()} OR {q.strip()}) AND ({p.strip()} OR {r.strip()}))"
                formula = formula.replace(match.group(0), replacement)
            else:
                break
        return formula
    
    def to_fnc(self, formula: str) -> str:
        """Converte a fórmula para FNC."""
        steps = [
            ('Eliminação de equivalências', self.eliminate_iff),
            ('Eliminação de implicações', self.eliminate_implies),
            ('Aplicação das leis de De Morgan', self.apply_de_morgan),
            ('Aplicação da distributividade', self.distribute_or)
        ]
        
        result = formula
        steps_log = []
        
        for step_name, step_func in steps:
            new_result = step_func(result)
            if new_result != result:
                steps_log.append((step_name, new_result))
            result = new_result
        
        return result, steps_log

    def process_formulas(self, input_file: str, output_file: str):
        """Processa as fórmulas do arquivo de entrada e gera as saídas."""
        try:
            # Lê o arquivo de entrada
            with open(input_file, 'r', encoding='utf-8') as f:
                n = int(f.readline().strip())
                formulas = [f.readline().strip() for _ in range(n)]
            
            # Processa cada fórmula
            results = []
            
            # Imprime cabeçalho
            self.print_header()
            
            for i, formula in enumerate(formulas, 1):
                # Converte para FNC
                parsed = self.parse_latex(formula)
                fnc_result, steps = self.to_fnc(parsed)
                latex_result = self.to_latex(fnc_result)
                
                # Adiciona ao resultado
                results.append(latex_result)
                
                # Imprime no terminal
                self.print_formula(i, formula, latex_result, steps)
            
            # Salva no arquivo de saída
            self.save_results(output_file, results)
            
            # Imprime rodapé
            self.print_footer(output_file)
            
        except FileNotFoundError:
            print(f"{self.colors['RED']}Erro: Arquivo {input_file} não encontrado.{self.colors['END']}")
        except Exception as e:
            print(f"{self.colors['RED']}Erro ao processar o arquivo: {str(e)}{self.colors['END']}")

    def print_header(self):
        """Imprime o cabeçalho do resultado."""
        print(f"\n{self.colors['BOLD']}{'=' * 60}{self.colors['END']}")
        print(f"{self.colors['BOLD']}Conversor de Fórmulas para Forma Normal Conjuntiva (FNC){self.colors['END']}")
        print(f"{self.colors['BOLD']}{'=' * 60}{self.colors['END']}\n")

    def print_formula(self, index: int, original: str, fnc: str, steps: List[Tuple[str, str]]):
        """Imprime uma fórmula e sua conversão FNC formatada."""
        print(f"{self.colors['BOLD']}Fórmula {index}:{self.colors['END']}")
        print(f"{self.colors['BLUE']}Original:{self.colors['END']} {self.to_unicode(original)}")
        
        # Imprime os passos intermediários
        if steps:
            print(f"{self.colors['YELLOW']}Passos intermediários:{self.colors['END']}")
            for step_name, step_result in steps:
                print(f"  {step_name}: {self.to_unicode(self.to_latex(step_result))}")
        
        print(f"{self.colors['GREEN']}FNC final:{self.colors['END']} {self.to_unicode(fnc)}")
        print(f"{self.colors['BOLD']}{'-' * 60}{self.colors['END']}\n")

    def print_footer(self, output_file: str):
        """Imprime o rodapé com informações adicionais."""
        print(f"{self.colors['BOLD']}Processamento concluído{self.colors['END']}")
        print(f"Resultados salvos em: {self.colors['UNDERLINE']}{output_file}{self.colors['END']}\n")

    def save_results(self, output_file: str, results: List[str]):
        """Salva os resultados no arquivo de saída."""
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(f"{len(results)}\n")
            for result in results:
                f.write(f"{result}\n")

def main():
    # Habilita suporte a cores ANSI no Windows
    if os.name == 'nt':
        os.system('color')
    
    # Arquivos de entrada e saída
    input_file = "input.txt"
    output_file = "output.txt"
    
    # Cria e executa o conversor
    converter = FNCConverter()
    converter.process_formulas(input_file, output_file)

if __name__ == "__main__":
    main()