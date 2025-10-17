
import argparse
import sys
from pathlib import Path

try:
	import yt_dlp
except Exception as e:
	print("yt-dlp is required. Install with: pip install yt-dlp")
	raise


def download_audio_mp3(url: str, outdir: Path):
	"""Download a single video/audio URL and convert to MP3 into outdir."""
	outdir.mkdir(parents=True, exist_ok=True)
	# yt-dlp options: extract audio, convert to mp3 using ffmpeg, best audio
	ydl_opts = {
		'format': 'bestaudio/best',
		'outtmpl': str(outdir / '%(title)s - %(id)s.%(ext)s'),
		'postprocessors': [{
			'key': 'FFmpegExtractAudio',
			'preferredcodec': 'mp3',
			'preferredquality': '192',
		}],
		'quiet': False,
		'noplaylist': True,
		'ignoreerrors': True,
		'no_warnings': True,
		'progress_hooks': [progress_hook],
	}

	with yt_dlp.YoutubeDL(ydl_opts) as ydl:
		ydl.download([url])


def download_playlist(playlist_url: str, outdir: Path):
	"""Download all items from a playlist or channel URL."""
	outdir.mkdir(parents=True, exist_ok=True)
	ydl_opts = {
		'format': 'bestaudio/best',
		'outtmpl': str(outdir / '%(playlist_index)03d - %(title)s - %(id)s.%(ext)s'),
		'postprocessors': [{
			'key': 'FFmpegExtractAudio',
			'preferredcodec': 'mp3',
			'preferredquality': '192',
		}],
		'ignoreerrors': True,
		'no_warnings': True,
		'progress_hooks': [progress_hook],
	}

	with yt_dlp.YoutubeDL(ydl_opts) as ydl:
		ydl.download([playlist_url])


def progress_hook(d):
	status = d.get('status')
	if status == 'downloading':
		tmpl = d.get('filename') or d.get('tmpfilename')
		downloaded = d.get('downloaded_bytes')
		total = d.get('total_bytes') or d.get('total_bytes_estimate')
		if downloaded and total:
			pct = downloaded / total * 100
			print(f"Downloading {tmpl}: {pct:.1f}%", end='\r')
	elif status == 'finished':
		print(f"\nFinished downloading: {d.get('filename')}")


def main(argv=None):
	parser = argparse.ArgumentParser(description='Download YouTube audio as MP3')
	group = parser.add_mutually_exclusive_group(required=True)
	group.add_argument('--url', help='YouTube video URL')
	group.add_argument('--playlist', help='YouTube playlist or channel URL')
	parser.add_argument('--out', '-o', default='downloads', help='Output directory')
	args = parser.parse_args(argv)

	outdir = Path(args.out)

	try:
		if args.url:
			print('Downloading single URL to', outdir)
			download_audio_mp3(args.url, outdir)
		elif args.playlist:
			print('Downloading playlist to', outdir)
			download_playlist(args.playlist, outdir)
	except KeyboardInterrupt:
		print('\nCancelled by user')
	except Exception as exc:
		print('Error:', exc)
		sys.exit(1)


if __name__ == '__main__':
	main()

from pytube import Playlist

# Your playlist URL
playlist_url = 'https://youtu.be/dY0b8Cj8BtM?si=-VOm3WMkjPD1g_Q3'
playlist = Playlist(playlist_url)

