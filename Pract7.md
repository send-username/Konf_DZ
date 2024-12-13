# Практическое занятие №7. Генераторы документации

## Задача 1

Реализовать с помощью математического языка LaTeX нижеприведенную формулу:

![image](https://github.com/user-attachments/assets/4a986823-dfe7-45f2-8900-f68dbc259843)

Прислать код на LaTeX и картинку-результат, где, помимо формулы, будет указано ФИО студента.

## Решение

\documentclass{article}
\usepackage[utf8]{inputenc}
\usepackage[russian]{babel}
\usepackage{amsmath}
\usepackage[T2A]{fontenc}
\begin{document}


\[
\int_{x}^{\infty} \frac{dt}{t(t^2 - 1) \log t} = \int_{x}^{\infty} \frac{1}{t \log t} \left( \sum_{m=1}^{\infty} t^{-2m} \right) dt = \sum_{m=1}^{\infty} \int_{x}^{\infty} \frac{t^{-2m}}{t \log t} dt = \sum_{m=1}^{\infty} \operatorname{li}(x^{-2m})
\]

Абдырахманов Юсуп

\end{document}


## Результат

![image](https://github.com/user-attachments/assets/94df678a-902b-489d-9edb-4c6cde8a6770)

## Задача 2

На языке PlantUML реализовать диаграмму на рисунке ниже. Прислать текст на PlantUML и картинку-результат, в которой ФИО студента заменены Вашими собственными.
Обратите внимание на оформление, желательно придерживаться именно его, то есть без стандартного желтого цвета и проч. Чтобы много не писать используйте псевдонимы с помощью ключевого слова "as".

Используйте [онлайн-редактор](https://plantuml-editor.kkeisuke.com/).

![image](https://github.com/user-attachments/assets/819c2b33-af34-45c6-82b7-4b75bcd0afa7)

## Решение

@startuml
skinparam lifelineStrategy nosolid
actor "Студент Абдырахманов Ю." as S
database Piazza as P
actor Преподаватель as T

T -> P : Публикация задачи
activate P
P --> T : Задача опубликована
deactivate P
...
S -> P : Поиск задач
activate P
P --> S : Получение задачи
deactivate P
...
S -> P : Публикация решения
activate P
P --> S : Решение опубликовано
deactivate P
...
T -> P : Поиск решений
activate P
P --> T : Решение найдено
T -> P : Публикация оценки
P --> T : Оценка опубликована
deactivate P
...
S -> P : Проверка оценки
activate P
P --> S : Оценка получена
deactivate P
@enduml


## Результат

![image](https://github.com/user-attachments/assets/6c6b6f15-4e28-4ebe-a6a0-b33be8cbe819)

## Задача 3

Описать какой-либо алгоритм сортировки с помощью noweb. Язык реализации не важен. Прислать nw-файл, pdf-файл и файл с исходным кодом. В начале pdf-файла должно быть указано ваше авторство. Добавьте, например, где-то в своем тексте сноску: \footnote{Разработал Фамилия И.О.}
Дополнительное задание: сравните "грамотное программирование" с Jupyter-блокнотами (см. https://github.com/norvig/pytudes/blob/master/ipynb/BASIC.ipynb), опишите сходные черты, различия, перспективы того и другого.

## Решение

```LaTeX
\documentclass{report}
\usepackage[utf8]{inputenc}
\usepackage[russian]{babel}
\usepackage{listings}  % Подключение пакета для кода

\begin{document}

\chapter{Алгоритм сортировки слиянием}

Этот документ описывает алгоритм сортировки слиянием с использованием noweb.

\section{Описание алгоритма}

Алгоритм сортировки слиянием разделяет список на две половины, рекурсивно сортирует их, а затем сливает отсортированные половины.

\subsection{Шаги алгоритма}

1. Разделить список на две половины.
2. Рекурсивно отсортировать каждую из половин.
3. Слить отсортированные половины в один отсортированный список.

\section{Исходный код}

\subsection{Функция слияния}

\begin{lstlisting}[language=Haskell]
merge :: Ord a => [a] -> [a] -> [a]
merge [] ys = ys
merge xs [] = xs
merge (x:xs) (y:ys)
  | x < y     = x : merge xs (y:ys)
  | otherwise = y : merge (x:xs) ys
\end{lstlisting}

\subsection{Основная функция сортировки слиянием}

\begin{lstlisting}[language=Haskell]
mergeSort :: Ord a => [a] -> [a]
mergeSort [] = []
mergeSort [x] = [x]
mergeSort xs = merge (mergeSort left) (mergeSort right)
  where
    (left, right) = splitAt (length xs div 2) xs
\end{lstlisting}
\footnote{Разработал Абдырахманов Ю.} 
\section{Заключение}

Алгоритм сортировки слиянием эффективно сортирует
