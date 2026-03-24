╔════════════════════════════════════════════════╗
║              Conway's Game of Life             ║
║                                                ║
║                                                ║
║        ╔════════════════════════════╗          ║
║        ║        · · · · · ·         ║          ║
║        ║      · · █ · █ · ·         ║          ║
║        ║      · █ █ █ █ █ ·         ║          ║
║        ║      · █ █ █ █ █ ·         ║          ║
║        ║      · · █ █ █ · ·         ║          ║
║        ║        · · █ · ·           ║          ║
║        ║          · · ·             ║          ║
║        ╚════════════════════════════╝          ║
║                                                ║
║        █ — live cell    · — dead cell          ║
║                                                ║
╚════════════════════════════════════════════════╝


# Case-14
The project was carried out by Alexey Simonov (role A: input/output and initialization and role B: game logic), Maria Fedotova (role C: mapping and role D: integration of all modules).

The program implements Conway's Game of Life, a classic cellular automaton. It simulates the evolution of a rectangular grid of cells, where each cell can be alive or dead. The next generation is determined by the number of live neighbors according to Conway's rules: a live cell with 2 or 3 live neighbors survives; a dead cell with exactly 3 live neighbors becomes alive; all other cells die or remain dead. The program provides an interactive graphical interface built with Pygame. Users can set the grid size, draw initial configurations with mouse clicks, generate random states, load/save configurations from/to text files, and control the simulation (start/pause, step, speed adjustment, reset, clear). The current generation number, simulation speed, and running status are displayed on the screen. The program supports toroidal (wrap-around) boundaries.

Проект выполнили: Симонов Алексей (роль A: ввод/вывод и инициализация и роль B: логика игры), Федотова Мария (роль C: отображение и роль D: интеграция всех модулей).

Программа реализует классический клеточный автомат «Игра Жизнь» Джона Конвея. Она моделирует эволюцию клеток на прямоугольной сетке, где каждая клетка может быть живой или мёртвой. Следующее поколение определяется количеством живых соседей по правилам Конвея: живая клетка с 2–3 живыми соседями остаётся живой; мёртвая клетка с ровно 3 живыми соседями становится живой; все остальные клетки умирают или остаются мёртвыми. Программа предоставляет интерактивный графический интерфейс на Pygame. Пользователь может задавать размер сетки, рисовать начальные конфигурации мышью, генерировать случайные состояния, загружать и сохранять конфигурации в текстовые файлы, управлять симуляцией (запуск/пауза, пошаговый режим, регулировка скорости, сброс, очистка). Номер текущего поколения, скорость симуляции и статус отображаются на экране.

