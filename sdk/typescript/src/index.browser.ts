import { loadData } from './data/browser';
import { createConverter as createCoreConverter } from './core/converter';
import type {
  Converter,
  ConverterOptions,
  Match,
  LookupResult,
  ConversionDetail,
  Source,
  ZhtwData,
} from './core/types';

let cachedData: ZhtwData | null = null;
let defaultConverter: Converter | null = null;

function getData(): ZhtwData {
  if (!cachedData) cachedData = loadData();
  return cachedData;
}

function getDefault(): Converter {
  if (!defaultConverter) defaultConverter = createCoreConverter(getData());
  return defaultConverter;
}

export function convert(text: string): string {
  return getDefault().convert(text);
}

export function check(text: string): Match[] {
  return getDefault().check(text);
}

export function lookup(word: string): LookupResult {
  return getDefault().lookup(word);
}

export function createConverter(options: ConverterOptions = {}): Converter {
  return createCoreConverter(getData(), options);
}

export type {
  Converter,
  ConverterOptions,
  Match,
  LookupResult,
  ConversionDetail,
  Source,
};
