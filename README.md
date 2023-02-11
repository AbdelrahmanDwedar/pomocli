# PomoCLI

PomoCLI is a simple CLI tool that counts the time of work and rest for you following the [Pomorodo technique](https://en.wikipedia.org/wiki/Pomodoro_Technique), that'll help you focus on doing one thing for 25 minutes and give you a rest of 5 minutes (you can disable that and make it only for work time).

---

## Installation

### Manual build

```bash
pip install -r requirements.txt

python3 -m setup.py # Linux and unit based
py -m setup.py # windows PowerShell
```

---

## Usage

### Modes

#### Normal Mode
Normal mode is the mode that will give you 25 minutes time for work, then give you a 5 minute resting time, then repeat till you stop it.

You can use the normal mode by not adding any flags at all or adding the `-n` flag.

```bash
pomocli -n
```

#### Work only mode
The work only mode is basically a mode where you just have a timer that gives you 25 minutes and then stop working and quit the application.

You can use the work only mode by adding the `--work-only` or `-w` flag.

```bash
pomocli --work-only
pomocli -w
```

### Time templates

You can set your own template or option of time stamp you want to use. for example you can have 60 minute work time with 15 minutes rest time.

#### Table of available time stamps

| Template name     | Time of work (in minutes) | Time of rest (in minutes)|
|:------------------|:--------------------------|:-------------------------|
| Tripartite (Trip) | 180                       | 30                       |
| Single            | 60                        | 15                       |
| Half              | 30                        | 7                        |
| Normal            | 25                        | 5                        |
| Quarterly         | 15                        | 2                        |

### Usage

You can use the `--stamp` or `-s` followed by the stamp you need.

```bash
pomocli --stamp "tripartite"
pomocli --stamp "trip"
pomocli --stamp "single"
pomocli --stamp "half"
pomocli --stamp "normal" # default
pomocli --stamp "quarterly"
pomocli --stamp "quar"
# or
pomocli -s "tripartite"
pomocli -s "trip"
pomocli -s "single"
pomocli -s "half"
pomocli -s "normal" # default
pomocli -s "quarterly"
pomocli -s "quar"
```

---

## Tech Stack

- Language: [Python](https://www.python.org/)
- Framework: [click](https://pypi.org/project/click/)

---

## Contribute 

You'll need some understanding of [Python](https://www.python.org/) and virtual environments and the [click](https://pypi.org/project/click/) module to understanding the code.

For more information about the contributing process go to [CONTRIBUTE.md](./CONTRIBUTE.md).
