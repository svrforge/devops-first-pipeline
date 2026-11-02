# Language support

| Area | English (default) | Tamil |
|---|---|---|
| Course navigation | Complete | Available |
| 12 module concepts | Complete | Available |
| CLI lesson headings | Complete | Module titles and concepts |
| Commands | English/shared | Identical commands |
| Detailed verification and failure exercises | Complete | English text with Tamil labels |
| Quizzes and tooling errors | English | English fallback |
| Extended labs and capstones | English | Not yet translated |

This is bilingual learning support, not a claim that every document is fully translated. The catalog explicitly declares `en` as default. Use `python learn.py --lang ta lesson 01` for Tamil concepts.

To improve translations: edit `course/catalog.json`, update the corresponding `docs/ta/NN.md`, retain valid commands and lesson IDs, then run `python scripts/validate_course.py` and all tests. Open a PR describing translation scope. Do not label a language complete until its full learning path has been reviewed by a fluent speaker. No machine translation service or API key is required.
