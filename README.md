# django 
# python

 # Etapas para o desenvolvimento da plataforma de empréstimo:

# Interface Web:

Desenvolva uma interface web intuitiva e responsiva, onde os solicitantes de empréstimo poderão preencher as informações necessárias para a solicitação da proposta.
Não será necessário implementar um sistema de autenticação. Qualquer pessoa poderá acessar a interface e preencher o pedido.
Configuração dos Campos da Proposta:

Crie um painel de configurações acessível apenas ao administrador do sistema, que permite definir quais campos devem ser solicitados aos solicitantes de empréstimo.
Essa interface de configuração deve ser flexível o suficiente para adicionar, remover ou modificar os campos da proposta conforme necessário.
Avaliação Automática da Proposta:

Utilize uma API de Análise de Crédito disponível em https://loan-processor.digitalsys.com.br/swagger/index.html ↗ para realizar a avaliação automática da proposta.
Integre a API ao sistema, enviando os dados da proposta e processando a resposta retornada pela API.
Se a API retornar um status de não aprovado, a proposta deverá ser negada automaticamente.
Se a API retornar um status de aprovado, a proposta deverá ser marcada para avaliação humana.
Lista e Status das Propostas:

Crie uma página de listagem no sistema, acessível apenas ao administrador, onde todas as propostas serão exibidas.
As propostas marcadas para avaliação humana deverão ser destacadas.
O administrador deve ter a capacidade de alterar o status das propostas para 'Aprovada' ou 'Negada' diretamente na listagem.
Estas são apenas sugestões iniciais para o desenvolvimento da plataforma de empréstimo. É importante adaptar e personalizar a implementação de acordo com as necessidades específicas da Loans For Good (LFG) e dos usuários no Brasil.
