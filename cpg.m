% Code to find out whether a given sequence is a CpG island or not
clc;
% Transition matrices for CpG sequences 
CpG_Tr = [0.180, 0.274, 0.426, 0.120; 0.171, 0.368, 0.274, 0.188; 0.161, 0.339, 0.375, 0.125; 0.079, 0.355, 0.384, 0.182];
% Transition matrices for CpG sequences
Non_CpG_Tr = [0.300, 0.205, 0.285, 0.210; 0.322, 0.298, 0.078, 0.302; 0.248, 0.246, 0.298, 0.208; 0.177, 0.239, 0.292, 0.292];

% User Input of DNA sequence
prompt = 'Enter DNA Sequence: ';
X = input(prompt, 's');

% Mapping of the nucleotide bases to the matrice indices 
Map = containers.Map({'a', 't', 'g', 'c'}, {1, 2, 3, 4});

log_LR = 0;

% Calculating the log likelihood ratio 
for k = 1:length(X)-1
    
    p_CpG = CpG_Tr(cell2mat(values(Map, {X(k)})), cell2mat(values(Map, {X(k+1)})));
    p_nCpG = Non_CpG_Tr(cell2mat(values(Map, {X(k)})), cell2mat(values(Map, {X(k+1)})));
    
    LR = p_CpG/p_nCpG;
    
    log_LR = log_LR + log10(LR);
end

if (log_LR < 0)
    disp('No. Sequence is a non-CpG Island.');
else
    disp('Yes. Sequence is a CpG Island.');
end 