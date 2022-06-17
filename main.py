from datetime import datetime
from os import listdir, makedirs, path
from pathlib import Path as pathlib
from shutil import move


class FileOrganizer:
    """Organize files of given location or downloads directory."""

    IMAGE_EXT = [".jpg", ".png", ".jpeg", ".gif", ".webp", ".eps"]
    DOC_EXT = [
        ".doc",
        ".docx",
        ".xls",
        ".xlsx",
        ".ppt",
        ".pptx",
        ".pdf",
        ".txt",
        ".odt",
        ".ods",
        ".epub",
        ".pages",
        ".pub",
        ".word",
        ".md",
        ".mdx",
        ".dot",
        ".dotx",
    ]
    VIDEO_EXT = [
        ".mp4",
        ".mov",
        ".avi",
        ".wmv",
        ".avchd",
        ".flv",
        ".f4v",
        ".swf",
        ".mkv",
        ".webm",
        ".mpeg-2",
    ]
    MUSIC_EXT = [
        ".mp3",
        ".aac",
        ".flac",
        ".alac",
        ".wav",
        ".aiff",
        ".dsd",
        ".pcm",
        ".ogg",
        ".wma",
    ]
    ZIP_EXT = [
        ".7z",
        ".gzip",
        ".zip",
        ".xz",
        ".bzip2",
        ".rar",
        ".rar5",
        ".tar",
        ".cab",
        ".lha",
        ".tgz",
    ]

    def __init__(self, location=None, option=1):
        self.location = location if location else str(pathlib.home() / "Downloads")
        self.option = option

        self.image_file_list = []
        self.doc_file_list = []
        self.video_file_list = []
        self.music_file_list = []
        self.zip_file_list = []
        self.other_file_list = []
        self.dir_list = []
        
        complete_list = listdir(self.location)
        self.make_file_list(complete_list)

    def make_file_list(self, complete_list: list):
        """Return list of files and directory based on passed list."""
        for file in complete_list:
            file_path = path.join(self.location, file)
            if path.isfile(file_path):
                file_ext = (path.splitext(file)[1]).lower()
                if file_ext in FileOrganizer.IMAGE_EXT:
                    self.image_file_list.append(file_path)
                elif file_ext in FileOrganizer.DOC_EXT:
                    self.doc_file_list.append(file_path)
                elif file_ext in FileOrganizer.VIDEO_EXT:
                    self.video_file_list.append(file_path)
                elif file_ext in FileOrganizer.MUSIC_EXT:
                    self.music_file_list.append(file_path)
                elif file_ext in FileOrganizer.ZIP_EXT:
                    self.zip_file_list.append(file_path)
                else:
                    self.other_file_list.append(file_path)
            else:
                self.dir_list.append(file_path)

    def check_directory(self, dir_location: str):
        """Check if directory exists or not. If not create one."""
        if not path.exists(dir_location):
            makedirs(dir_location)

    def get_file_creation_date(self, file_path):
        """get creation time of file and return string format"""
        c_time = path.getctime(file_path)
        date_time = datetime.utcfromtimestamp(c_time)
        formated_date = date_time.strftime("%Y/%m")
        return formated_date

    def file_mover(self, file_list, new_location):
        """move file based on extension list to new location."""
        for file in file_list:
            # Organize file based on creation year, month and file type
            end_path = path.join(
                self.location, self.get_file_creation_date(file), new_location
            )
            if self.option == 2:
            # Organize file based on file type
                end_path = path.join(self.location, new_location)
            if self.option == 3:
            # Organize file based on creation year, month
                end_path = path.join(self.location, self.get_file_creation_date(file))
            self.check_directory(end_path)
            move(file, end_path)

    def organize_images(self):
        """Organize images based on jpg, jpeg, png, gif, webp extensions."""

        self.file_mover(self.image_file_list, "Organized Images")

    def organize_docs(self):
        """Organize images based on jpg, jpeg, png, gif, webp extensions."""

        self.file_mover(self.doc_file_list, "Organized Documents")

    def organize_videos(self):
        """Organize images based on jpg, jpeg, png, gif, webp extensions."""

        self.file_mover(self.video_file_list, "Organized Videos")

    def organize_music(self):
        """Organize images based on jpg, jpeg, png, gif, webp extensions."""

        self.file_mover(self.music_file_list, "Organized Musics")

    def organize_zip(self):
        """Organize images based on jpg, jpeg, png, gif, webp extensions."""

        self.file_mover(self.zip_file_list, "Organized Zip Files")

    def organize_others(self):
        """Organize images based on jpg, jpeg, png, gif, webp extensions."""

        self.file_mover(self.other_file_list, "Organized Other Files")

    def call_all(self):
        """Call all mover methods"""
        self.organize_images()
        self.organize_docs()
        self.organize_music()
        self.organize_videos()
        self.organize_zip()
        self.organize_others()


FileOrganizer(option=3).call_all()
