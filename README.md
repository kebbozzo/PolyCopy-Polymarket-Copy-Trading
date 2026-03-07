% !TEX program = xelatex
\documentclass[11pt]{article}
\usepackage{geometry}
\geometry{a4paper, margin=2.5cm}
\usepackage{fontspec}
\setmainfont{Source Sans Pro}[
  Extension=.ttf,
  UprightFont=*,
  BoldFont=*Bold,
  ItalicFont=*Italic
]
\usepackage{titlesec}
\usepackage{listings}
\usepackage{xcolor}
\usepackage{hyperref}
\usepackage{enumitem}

% Definizione dei colori per il codice
\definecolor{codebg}{rgb}{0.95,0.95,0.95}
\definecolor{comment}{rgb}{0.2,0.6,0.2}
\definecolor{keyword}{rgb}{0.1,0.3,0.8}
\definecolor{string}{rgb}{0.8,0.2,0.2}

% Stile per listings
\lstset{
    backgroundcolor=\color{codebg},
    basicstyle=\ttfamily\small,
    breaklines=true,
    commentstyle=\color{comment},
    keywordstyle=\color{keyword}\bfseries,
    stringstyle=\color{string},
    frame=single,
    numbers=left,
    numberstyle=\tiny\color{gray},
    stepnumber=1,
    tabsize=4,
    showstringspaces=false,
    captionpos=b,
    language=bash
}

% Personalizzazione titoli
\titleformat{\section}{\Large\bfseries\color{blue!60!black}}{\thesection}{1em}{}
\titleformat{\subsection}{\large\bfseries\color{blue!50!black}}{\thesubsection}{1em}{}

% Metadata
\title{\Huge\textbf{PolyCopy-Copy-Trading} \\ \large Un bot per copiare automaticamente operazioni su Polymarket}
\author{}
\date{\today}

\begin{document}

\maketitle

\begin{abstract}
Un bot Python che monitora wallet specificati su Polymarket e copia automaticamente le loro attività di trading. Rileva variazioni nelle posizioni (apertura, chiusura, incremento, decremento) ed esegue le stesse operazioni utilizzando il tuo account.
\end{abstract}

\section*{Caratteristiche principali}
\begin{itemize}[noitemsep, topsep=0pt]
    \item Monitoraggio simultaneo di più indirizzi wallet.
    \item Rilevamento in tempo reale di cambiamenti nelle posizioni.
    \item Copia automatica delle operazioni con percentuale personalizzabile.
    \item Limite di richieste configurabile per rispettare le API.
    \item Possibilità di disattivare il trading reale (modalità log).
\end{itemize}

\section*{Setup}

\subsection*{1. Installa le dipendenze}
\begin{lstlisting}[language=bash]
pip install -r requirements.txt
\end{lstlisting}

\subsection*{2. Crea un file \texttt{.env} con le tue credenziali}
\begin{lstlisting}[language=bash]
POLYMARKET_PRIVATE_KEY=your_private_key
POLYMARKET_PROXY_ADDRESS=your_proxy_address
\end{lstlisting}

\subsection*{3. Configura \texttt{config.json}}
\begin{lstlisting}[language=json]
{
    "wallets_to_track": ["0x..."],
    "copy_percentage": 1.0,
    "rate_limit": 25,
    "trading_enabled": true
}
\end{lstlisting}

\section*{Parametri di configurazione}
\begin{description}[style=nextline]
    \item[\texttt{wallets\_to\_track}] Lista degli indirizzi wallet da seguire.
    \item[\texttt{copy\_percentage}] Percentuale di copia rispetto alla dimensione originale (es. 1.0 = 100\%, 0.2 = 20\%, 2.0 = 200\%).
    \item[\texttt{rate\_limit}] Numero massimo di richieste API consentite in una finestra di 10 secondi (default: 25).
    \item[\texttt{trading\_enabled}] Se \texttt{false}, il bot si limita a registrare le operazioni senza eseguirle.
\end{description}

\section*{Esecuzione}
\begin{lstlisting}[language=bash]
python src/main.py
\end{lstlisting}

\vfill
\begin{center}
    \textbf{Nota:} Assicurati di avere i moduli \texttt{src.positions} e \texttt{src.trading} nella struttura del progetto.
\end{center}

\end{document}
