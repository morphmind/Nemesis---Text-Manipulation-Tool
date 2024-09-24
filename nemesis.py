import os
from colorama import init, Fore, Style

# Initialize colorama for cross-platform colored terminal text
# Platformlar arası renkli terminal metni için colorama'yı başlat
init()

# Language dictionaries / Dil sözlükleri
ENGLISH = {
    "select_language": "Select your language / Dilinizi seçin:\n1. English\n2. Türkçe\nYour choice / Seçiminiz (1/2): ",
    "invalid_language": "Invalid selection. Please try again. / Geçersiz seçim. Lütfen tekrar deneyin.",
    "available_files": "Available files:",
    "select_file": "Select the file to process (enter number) or type a new file name: ",
    "invalid_selection": "Invalid selection. Please try again.",
    "enter_text": "Enter the text to process (Enter 'q' to return to main menu): ",
    "select_operation": "Choose the operation you want to perform:\n1. Remove word\n2. Replace word\n3. Add text to beginning or end of lines\nYour choice (1, 2 or 3): ",
    "enter_text_to_remove": "Enter the text to remove: ",
    "enter_text_to_replace": "Enter the text to replace: ",
    "enter_new_text": "Enter the new text: ",
    "add_position": "Where do you want to add the text?\n1. Beginning of lines\n2. End of lines\nYour choice (1 or 2): ",
    "enter_text_to_add": "Enter the text to add: ",
    "invalid_position": "Invalid selection. Please enter '1' or '2'.",
    "file_exists": "The file '{}' already exists. Do you want to overwrite it? (y/n): ",
    "operation_cancelled": "Operation cancelled.",
    "processed_lines": "Processed lines: {}, Processed text count: {}",
    "operation_completed": "Operation completed.",
    "total_processed_lines": "Total processed lines: {}",
    "total_processed_text": "Total processed text count: {}",
    "updated_content_saved": "Updated content saved to '{}'",
    "file_not_found": "Error: File '{}' not found.",
    "error_occurred": "An error occurred: {}",
    "process_another": "Do you want to process another file? (y/n): ",
    "program_terminating": "Program is terminating. Have a good day!",
    "another_operation": "Do you want to perform another operation on this file? (y/n): ",
    "operation_successful": "Operation completed successfully. Changes have been saved.",
    "operation_failed": "Operation failed. No changes were made.",
    "change_file": "Do you want to change the file for the next operation? (y/n): ",
}

TURKISH = {
    "select_language": "Select your language / Dilinizi seçin:\n1. English\n2. Türkçe\nYour choice / Seçiminiz (1/2): ",
    "invalid_language": "Invalid selection. Please try again. / Geçersiz seçim. Lütfen tekrar deneyin.",
    "available_files": "Mevcut dosyalar:",
    "select_file": "İşlem yapmak istediğiniz dosyayı seçin (numara girin) veya yeni dosya adı yazın: ",
    "invalid_selection": "Geçersiz seçim. Lütfen tekrar deneyin.",
    "enter_text": "İşlem yapılacak metni girin (Ana menüye dönmek için 'q' girin): ",
    "select_operation": "Yapmak istediğiniz işlemi seçin:\n1. Kelime kaldır\n2. Kelime değiştir\n3. Satırların başına veya sonuna metin ekle\nSeçiminiz (1, 2 veya 3): ",
    "enter_text_to_remove": "Kaldırılacak metni girin: ",
    "enter_text_to_replace": "Değiştirilecek metni girin: ",
    "enter_new_text": "Yeni metni girin: ",
    "add_position": "Metni nereye eklemek istersiniz?\n1. Satırların başına\n2. Satırların sonuna\nSeçiminiz (1 veya 2): ",
    "enter_text_to_add": "Eklenecek metni girin: ",
    "invalid_position": "Geçersiz seçim. Lütfen '1' veya '2' girin.",
    "file_exists": "'{}' dosyası zaten mevcut. Üzerine yazmak istiyor musunuz? (e/h): ",
    "operation_cancelled": "İşlem iptal edildi.",
    "processed_lines": "İşlenen satır: {}, İşlenen metin sayısı: {}",
    "operation_completed": "İşlem tamamlandı.",
    "total_processed_lines": "Toplam işlenen satır: {}",
    "total_processed_text": "Toplam işlenen metin sayısı: {}",
    "updated_content_saved": "Güncellenmiş içerik '{}' dosyasına kaydedildi.",
    "file_not_found": "Hata: {} dosyası bulunamadı.",
    "error_occurred": "Bir hata oluştu: {}",
    "process_another": "Başka bir dosya üzerinde işlem yapmak istiyor musunuz? (e/h): ",
    "program_terminating": "Program sonlandırılıyor. İyi günler!",
    "another_operation": "Bu dosya üzerinde başka bir işlem yapmak istiyor musunuz? (e/h): ",
    "operation_successful": "İşlem başarıyla tamamlandı. Değişiklikler kaydedildi.",
    "operation_failed": "İşlem başarısız oldu. Hiçbir değişiklik yapılmadı.",
    "change_file": "Bir sonraki işlem için dosyayı değiştirmek istiyor musunuz? (e/h): ",
}

def select_language():
    # Function to select the language for the program
    # Programın dilini seçmek için fonksiyon
    while True:
        choice = input(ENGLISH["select_language"])
        if choice == "1":
            return ENGLISH
        elif choice == "2":
            return TURKISH
        else:
            print(Fore.RED + ENGLISH["invalid_language"] + Style.RESET_ALL)

def generate_output_filename(old_text, new_text, operation):
    # Generate a filename for the output based on the operation
    # İşleme göre çıktı için bir dosya adı oluştur
    def clean_text(text):
        return ''.join(c if c.isalnum() else '-' for c in text).strip('-')

    if operation == '1':  # Remove / Kaldır
        return f"remove-{clean_text(old_text)}.txt"
    elif operation == '2':  # Replace / Değiştir
        return f"change-{clean_text(old_text)}-to-{clean_text(new_text)}.txt"
    else:  # Add / Ekle
        return f"add-{clean_text(new_text)}.txt"

def process_text_in_file(input_file_path, output_file_path, old_text, new_text, operation, position='', lang=ENGLISH):
    # Process the text in the input file and write to the output file
    # Girdi dosyasındaki metni işle ve çıktı dosyasına yaz
    try:
        with open(input_file_path, 'r', encoding='utf-8') as input_file:
            with open(output_file_path, 'w', encoding='utf-8') as output_file:
                line_count = 0
                processed_count = 0

                for line in input_file:
                    line_count += 1
                    if operation == '1':  # Remove / Kaldır
                        new_line = line.replace(old_text, '')
                        if new_line != line:
                            processed_count += 1
                    elif operation == '2':  # Replace / Değiştir
                        new_line = line.replace(old_text, new_text)
                        if new_line != line:
                            processed_count += 1
                    else:  # Add to beginning or end / Başına veya sonuna ekle
                        if position == '1':  # Beginning / Başına
                            new_line = new_text + line
                        else:  # End / Sonuna
                            new_line = line.rstrip() + new_text + '\n'
                        processed_count += 1

                    output_file.write(new_line)

                    if line_count % 100 == 0:
                        print(lang["processed_lines"].format(line_count, processed_count))

        print(f"\n{Fore.GREEN}{lang['operation_completed']}{Style.RESET_ALL}")
        print(lang["total_processed_lines"].format(line_count))
        print(lang["total_processed_text"].format(processed_count))
        print(f"{Fore.GREEN}{lang['updated_content_saved'].format(output_file_path)}{Style.RESET_ALL}")

    except FileNotFoundError:
        print(f"{Fore.RED}{lang['file_not_found'].format(input_file_path)}{Style.RESET_ALL}")
        return False
    except Exception as e:
        print(f"{Fore.RED}{lang['error_occurred'].format(e)}{Style.RESET_ALL}")
        return False

    return True

def select_file(lang):
    # Function to select a file for processing
    # İşlenecek dosyayı seçmek için fonksiyon
    while True:
        print(f"\n{lang['available_files']}")
        files = [f for f in os.listdir() if f.endswith('.txt')]
        for i, file in enumerate(files, 1):
            print(f"{i}. {file}")

        choice = input(f"\n{lang['select_file']}")

        if choice.isdigit() and 1 <= int(choice) <= len(files):
            return files[int(choice) - 1]
        elif choice.strip():
            if not choice.endswith('.txt'):
                choice += '.txt'
            return choice
        else:
            print(f"{Fore.RED}{lang['invalid_selection']}{Style.RESET_ALL}")

def main():
    # Main function to run the Nemesis program
    # Nemesis programını çalıştırmak için ana fonksiyon
    lang = select_language()

    while True:
        input_file_path = select_file(lang)

        while True:
            operation = input(lang["select_operation"])
            if operation not in ['1', '2', '3']:
                print(f"{Fore.RED}{lang['invalid_selection']}{Style.RESET_ALL}")
                continue

            position = ''  # Initialize position for all operations / Tüm işlemler için pozisyonu başlat
            if operation == '1':
                old_text = input(lang["enter_text_to_remove"])
                new_text = ''
            elif operation == '2':
                old_text = input(lang["enter_text_to_replace"])
                new_text = input(lang["enter_new_text"])
            else:  # operation == '3'
                old_text = "ADD_OPERATION"  # Used as a marker / İşaretçi olarak kullanılıyor
                position = input(lang["add_position"])
                while position not in ['1', '2']:
                    print(f"{Fore.RED}{lang['invalid_position']}{Style.RESET_ALL}")
                    position = input(lang["add_position"])
                new_text = input(lang["enter_text_to_add"])

            if old_text.lower() == 'q':
                break

            output_file_path = generate_output_filename(old_text, new_text, operation)

            if os.path.exists(output_file_path):
                overwrite = input(lang["file_exists"].format(output_file_path))
                if overwrite.lower() not in ['y', 'e']:
                    print(f"{Fore.YELLOW}{lang['operation_cancelled']}{Style.RESET_ALL}")
                    continue

            success = process_text_in_file(input_file_path, output_file_path, old_text, new_text, operation, position, lang)

            if success:
                print(f"{Fore.GREEN}{lang['operation_successful']}{Style.RESET_ALL}")
            else:
                print(f"{Fore.RED}{lang['operation_failed']}{Style.RESET_ALL}")

            another_operation = input(lang["another_operation"])
            if another_operation.lower() in ['y', 'e']:
                change_file = input(lang["change_file"])
                if change_file.lower() in ['y', 'e']:
                    break  # Break this inner loop and go to new file selection / Bu iç döngüyü kır ve yeni dosya seçimine git
            else:
                break  # Break this inner loop / Bu iç döngüyü kır

        process_another = input(f"\n{lang['process_another']}")
        if process_another.lower() not in ['y', 'e']:
            print(f"{Fore.GREEN}{lang['program_terminating']}{Style.RESET_ALL}")
            break

if __name__ == "__main__":
    main()
