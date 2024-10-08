Certainly! Here’s the complete setup in a copy-paste format:

### 1. `config.ini`

Create a file named `config.ini` with the following content:

```ini
# Condeco_Seatbooking_Script
# Automating the booking process because you prefer efficiency over manual tasks.

[credentials]
email = abc@def.com
password = abcdef

[urls]
login_url = https://pqr.condecosoftware.com/

[seating]
floor = 5
seatNo = AZ91
```

### 2. Instructions for Setting Up `chromedriver.exe`

1. Download ChromeDriver:
   - Go to the [ChromeDriver download page](https://sites.google.com/chromium.org/driver/downloads).
   - Download the version compatible with your version of Chrome.
   - Extract the `chromedriver.exe` file.

2. Place `chromedriver.exe` in the Root Directory:
   - Move the `chromedriver.exe` file to the root directory of your project (where `config.ini` is located).

### Summary

1. Create `config.ini` with the provided content.
2. Download and place `chromedriver.exe` in your project root directory.
3. Use the provided Python script to automate the booking process.
