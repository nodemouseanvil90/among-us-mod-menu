C++ helper for scanning stable memory offsets between Among Us updates.

Build (MSVC):
    cl /std:c++20 /O2 scanner.cpp /Fe:scanner.exe

Output: offsets_dump.json consumed by src/services/offset_db.py
This binary is intentionally NOT committed. Rebuild locally after each game patch.