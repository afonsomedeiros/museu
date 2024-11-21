# Projeto Museu.

## Ideia.

Trata-se de um projeto focado em uma galeria virtual para exposição de imagens.

O proposito do projeto é estudar e melhorar conhecimentos em recursos visuais utilizando uma arquitetura real.

## Entidades

- Usuario (users)
  - Nome
  - E-mail
  - Senha

- Exposição:
  - Titulo
  - Data de inicio
  - Data de Encerramento
  - Descrição.
  - Autor.

- Peça
  - Titulo
  - Descrição
  
- Foto
  - Foto
  - Descricao
  - Autor
  - Data Registro.

## Estrutura do projeto:

### Administrativo.

SubProjeto onde podem ser cadastrados novos usuários e realizar registros para as entidades do projeto.

### Museu.

SubProjeto onde se concentrarão os recursos visuais para apresentação das imagens da exposíção.

## Execução do projeto:

### Windows (Powershell)

```sh
> [System.Environment]::SetEnvironmentVariable('ENV','DEV')
> python main.py
```